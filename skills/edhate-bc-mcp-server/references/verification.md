# Verification scenarios

Use synthetic fixtures and mocked Business Central responses for repeatable development checks. Run live integration checks only against an authorized environment. State clearly which kind of evidence each test provides.

| Scenario | Expected evidence |
| --- | --- |
| Client initializes server | Successful negotiation with the target SDK/client |
| Client discovers tools | Names and schemas match the implemented handlers |
| Valid read invocation | Correct company, route, mapping, and bounded output |
| Malformed input | Rejected before an upstream request |
| Missing configuration | Actionable startup or invocation failure without secret exposure |
| Empty response | Distinguished from a failed API request |
| Expired token / forbidden operation | Appropriate recovery or denial, no retry loop |
| Untrusted continuation URL | Rejected without sending credentials |
| Throttling or timeout | Bounded retry for safe operations and useful failure |
| Write timeout after commit | Reconciliation rather than blind duplication |
| Concurrent users | No credential, company, or response leakage |
| stdio logging | Diagnostics do not corrupt protocol stdout |

## Skill evaluation prompts

Use these when reviewing changes to this skill; they are scenarios, not claims that evaluation has already run.

- Build a local MCP server exposing customer search from a supplied Business Central API fixture. Verify initialization, discovery, bounded search, and malformed input rejection.
- Add a sales-order creation tool to an existing server. Simulate a timeout after the remote write and verify that the implementation does not blindly retry.
- Adapt a server for two authenticated users with different company access. Verify that changing tool arguments cannot cross the configured authorization boundary.

A review should also confirm that unrelated requests to install an existing MCP server do not cause the assistant to scaffold a new implementation.
