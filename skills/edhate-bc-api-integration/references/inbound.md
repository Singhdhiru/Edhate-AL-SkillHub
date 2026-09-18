# Inbound integration decisions

Evaluate existing standard APIs against the requested entity, fields, and operations. Build a custom endpoint when requirements justify it.

Define the API contract before implementation: publisher, group, version, resource names, identifiers, writable fields, supported operations, related entities, and permissions. Distinguish standard API routing from custom API routing; verify the route against official documentation and the actual deployment.

Read object ranges from the consuming project. Do not prescribe a fixed range, force a version string, or copy properties without checking support in the project's runtime.

Specify which field and record validations execute for writes. Decide whether consumers may create, modify, or delete each resource. Do not grant write permissions for a read-only requirement.

Define concurrency behavior for updates, duplicate identification for creates, and expected error responses. Test relationships and filters if the endpoint exposes them. Test with the intended integration identity, not only an administrator.

Treat a published contract as a dependency for its consumers. Document compatibility implications when changing identifiers, field types, required fields, or operations.
