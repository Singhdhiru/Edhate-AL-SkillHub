# Business Central access

## Configuration and credentials

Establish the deployment type and API contract before composing routes. Keep tenant, environment, company identifier, and permitted endpoint origin in validated server configuration. Never take an unrestricted base URL from tool arguments.

Choose the authentication flow based on deployment and whether operations run as an application or delegated user. Verify supported Microsoft Entra configuration and Business Central permission requirements using official Microsoft documentation. Do not assume token issuance alone grants access to business data.

Keep secrets outside committed files and tool results. Separate token caches by the relevant identity and authorization context. Handle expiry and refresh without unbounded retries. Do not reuse one user's access token for another user.

## API client behavior

Reuse standard APIs where they satisfy the requirement. For custom APIs, inspect their actual publisher, group, version, fields, validation, and permissions. Do not reuse a standard route for a custom API or invent AL object IDs.

Validate pagination and redirect destinations against the configured trusted origin and permitted API scope before following them with credentials. Set bounded timeouts, maximum page sizes, and bounded retries appropriate to the operation.

A timed-out write may already have committed. Reconcile its outcome before retrying. Define duplicate prevention and concurrency handling according to the actual API contract. Do not label all POST operations safely retryable.

Preserve useful upstream error information while removing secrets and private payloads. Keep authentication failures, permission failures, missing records, throttling, validation errors, and service outages distinguishable.

## Write operations

Implement writes only within requested scope. Describe their effects, validate identifiers and writable fields, and apply server-side permissions. Financial posting, deletion, and bulk updates require deliberate product behavior and the user's authorization; an annotation or `confirmed=true` argument alone is not an authorization mechanism.
