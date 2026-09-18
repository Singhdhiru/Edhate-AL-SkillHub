# Outbound integration decisions

Read the external API contract before implementing calls. Record the operation, URL construction, required headers, authentication flow, payload schema, response schema, pagination contract, and documented limits. Use sanitized examples.

Separate credential acquisition from request mapping where the existing project allows it. Confirm supported secret-handling APIs against the target runtime. Never log authorization headers.

Specify how each response affects local business state. For a timed-out write, determine whether the remote operation completed before retrying. Use an API-supported idempotency key or reconciliation lookup where available. If neither exists, document the unresolved outcome and provide a controlled recovery path.

For paginated imports, define when a page is committed and when its checkpoint advances. A failed page must not cause unprocessed records to be skipped. Establish a duplicate-detection rule before enabling retries.

Prefer scheduled retry over holding an interactive request open for a long backoff. Follow the service's documented retry guidance and bound attempts. Distinguish an expired credential from insufficient permission; repeated authentication attempts do not fix a permission problem.

Deliver the setup fields, sanitized example payload, field mapping, status handling, and recovery procedure relevant to the requested operation.
