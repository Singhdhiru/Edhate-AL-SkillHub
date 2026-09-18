# Server design decisions

## Tool contracts

Use operation-specific names such as `list_customers` or `get_sales_order`. Establish required identifiers, permitted filters, page limits, output fields, and error behavior before writing handlers. A write tool must make its effect clear and validate all inputs before contacting Business Central.

Make tenant/environment/company selection explicit in configuration or authenticated context. Do not silently select the first company. For shared servers, bind allowed company scope to the authenticated principal and check it on every operation.

Avoid unrestricted query expressions and raw endpoint parameters. Map supported filters to validated API parameters and encode them correctly. Cap result size and expose a documented continuation mechanism rather than fetching unlimited pages into one tool response.

Use the selected SDK's supported result and error formats. Match declared schemas to actual results. Add truthful read-only or destructive annotations where supported, but enforce permissions in code regardless of annotations.

## Transport and lifecycle

Choose the transport supported by the actual client and SDK. A locally launched stdio server and a remotely hosted HTTP server have different lifecycle, credential, and authentication requirements; document the choice.

Keep stdio startup banners and diagnostics off stdout. Verify clean startup and shutdown, timeouts, cancellation where supported, and failure behavior when configuration is missing.

For remote hosting, verify the protocol's current authentication, origin validation, session handling, and transport requirements. Apply request limits and isolate concurrent users. Do not treat a session identifier as authorization. Use the deployment platform's secret management and logging conventions.

Separate client-to-MCP authorization from MCP-to-Business-Central authorization. Do not forward a client token to Business Central unless that audience and delegated flow are explicitly supported and validated.

## SDK selection

Inspect the repository lockfile and installed package API. Consult the official documentation matching that release. Prefer the SDK's protocol handling rather than hand-writing JSON-RPC framing. Provide only the configuration format supported by the requested client; do not imply one client configuration works everywhere.
