# Integration verification

Select cases relevant to the implemented operation. Record the input, expected result, actual result, and environment. Do not mark a scenario passed without execution evidence.

| Scenario | Observable outcome |
| --- | --- |
| Valid request | Correct record mapping and expected business validation |
| Missing or invalid value | Useful failure with no unintended partial change |
| Missing or expired credentials | No secret disclosure; documented recovery |
| Insufficient permission | Operation rejected under the intended identity |
| Empty or multi-page response | Correct completion and no skipped records |
| Rate limit or service outage | Bounded retry or recoverable failure |
| Timeout after a write | Reconciliation prevents blind duplicate creation |
| Repeated record or request | Defined duplicate behavior |
| Concurrent update | Defined conflict behavior |
| Partial batch failure | Checkpoint and recovery preserve unprocessed work |

Compile and run applicable project tests. If a sandbox or external service is unavailable, report those checks as not run. Keep synthetic payloads free of real customer data.
