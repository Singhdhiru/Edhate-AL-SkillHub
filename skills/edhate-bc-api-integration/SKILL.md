---
name: edhate-bc-api-integration
description: Build or update Business Central API integrations in AL. Use for outbound HTTP integrations, inbound API endpoints, and synchronization workflows that need authentication, data mapping, and failure handling.
---

# Edhate Business Central API Integration

Implement the requested integration using the target project's conventions and documented API contract. This initial skill defines general integration guidance; do not claim that unspecified choices are approved Edhate standards.

## Establish context

Read applicable repository instructions, `app.json`, and relevant existing integration code. Identify the target Business Central version, runtime, deployment type, object ranges, naming conventions, and available build tooling.

Determine whether data flows into Business Central, out of it, or both. Establish entities, field mappings, source of truth, execution method, expected volume, authentication requirements, and failure recovery expectations. Ask only for missing information that affects implementation.

Use the supplied API documentation and official Microsoft documentation when needed. Verify version-dependent features against the target environment. Never invent endpoints, payload fields, authentication flows, or business rules.

## Choose the integration approach

For inbound integrations, check whether standard Business Central APIs meet the requirement before adding custom endpoints. Define stable identifiers, exposed fields, permissions, validation behavior, and concurrency requirements.

For outbound integrations, reuse existing HTTP and authentication components when appropriate. Separate transport, payload mapping, and business processing where this makes the implementation easier to maintain. Follow the external API contract for headers, pagination, status codes, and rate limits.

For synchronization, establish identifier mapping, duplicate prevention, checkpoint handling, conflict resolution, and recovery after partial completion. Do not assume a timed-out write failed at the remote system.

## Implement safely and predictably

Keep customer endpoints and settings in project configuration. Do not hardcode credentials or include tokens or sensitive payloads in logs. Use credential handling supported by the target environment and project standards.

Distinguish transport failures from HTTP error responses. Retry only when the operation and contract make retries safe, with bounded attempts and appropriate delay. Account for ambiguous write results and duplicate creation.

Apply business validations deliberately when writing records. Consider transaction boundaries and avoid holding database locks during slow external operations where the architecture permits it. Use only the permissions the integration needs.

Do not add a scheduling framework, staging tables, or a new abstraction layer unless the requirements justify it.

## Validate and deliver

Compile with the project's available tools. Check representative success and failure cases relevant to the change, including mapping, authentication errors, pagination, throttling, and duplicate handling when applicable.

State which checks ran and which require a connected environment. Provide setup instructions without secrets, relevant mappings, and recovery notes proportional to the change.

A request to generate or review code does not itself authorize deployment or live data changes. Follow the user's existing authorization for those actions.
