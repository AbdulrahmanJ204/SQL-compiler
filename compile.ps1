

param(
    [Parameter(Position = 0)]
    [string]$TestName,
    
    [Parameter()]
    [switch]$ShowTokens
)

$SrcDir = "src"
$GenDir = "src/generated"
$TestsDir = ""

function Write-Success { Write-Host $args -ForegroundColor Green }
function Write-Info { Write-Host $args -ForegroundColor Yellow }
function Write-Error { Write-Host $args -ForegroundColor Red }

Write-Success "`n=== ANTLR T-SQL Parser Build Script ===`n"

if (-not (Test-Path $GenDir)) {
    Write-Info "Creating generated directory..."
    New-Item -ItemType Directory -Path $GenDir -Force | Out-Null
}

$initFile = Join-Path $GenDir "__init__.py"
if (-not (Test-Path $initFile)) {
    New-Item -ItemType File -Path $initFile -Force | Out-Null
}

Write-Info "Generating Lexer..."
antlr4 "$SrcDir/SQLLexer.g4" -Dlanguage=Python3 -o $GenDir

if ($LASTEXITCODE -ne 0) {
    Write-Error "✗ Lexer generation failed"
    exit 1
}
Write-Success "✓ Lexer generated successfully`n"

Write-Info "Generating Parser..."
antlr4 "$SrcDir/SQLParser.g4" -Dlanguage=Python3 -no-listener -visitor -o $GenDir

if ($LASTEXITCODE -ne 0) {
    Write-Error "✗ Parser generation failed"
    exit 1
}
Write-Success "✓ Parser generated successfully`n"

if ([string]::IsNullOrEmpty($TestName)) {
    Write-Info "No test file specified. Build complete."
    Write-Host "Usage: .\compile.ps1 <test_name> [-ShowTokens]"
    exit 0
}

$testFile = $TestName

if (-not (Test-Path $testFile)) {
    Write-Error "✗ Test file not found: $testFile"
    exit 1
}

Write-Info "Parsing file: $testFile`n"
Write-Success "--- Output ---"

if ($ShowTokens) {
    python "$SrcDir/main.py" $testFile --tokens
} else {
    python "$SrcDir/main.py" $testFile
}

if ($LASTEXITCODE -ne 0) {
    Write-Error "`n✗ Parsing failed"
    exit 1
}

Write-Success "`n=== Complete ==="