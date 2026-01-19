
OUTPUT DELETED.*``
OUTPUT INSERTED.*
OUTPUT INSERTED.id, INSERTED.name
OUTPUT INSERTED.id INTO @InsertedIds
OUTPUT DELETED.id, DELETED.name
OUTPUT DELETED.id INTO deleted_students_log
OUTPUT
  DELETED.* AS old_age,
  INSERTED.* AS new_age
OUTPUT
  DELETED.age,
  INSERTED.age
INTO age_changes(old_age, new_age)
OUTPUT
    INSERTED.id,
    DELETED.name,
    INSERTED.age + 1 AS computed_value,
    'UPDATED' AS action_type
OUTPUT INSERTED.*, DELETED.*
DECLARE @t TABLE (id INT)
OUTPUT DELETED.id INTO @t
