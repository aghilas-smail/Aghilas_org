import avro.schema
import avro.io
import avro.datafile
import io

schema_str = """
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "age", "type": "int"},
    {"name": "email", "type": ["null", "string"], "default": null}
  ]
}
"""
schema = avro.schema.parse(schema_str)

writer = avro.datafile.DataFileWriter(
    open("users.avro", "wb"),
    avro.io.DatumWriter(),
    schema
)

writer.append({"name": "Alice", "age": 30, "email": "alice@example.com"})
writer.append({"name": "Bob", "age": 25, "email": "bob@example.com"})
writer.close()
