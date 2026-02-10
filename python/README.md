# Nia AI Python SDK

The official Python SDK for the [Nia AI](https://trynia.ai) API. Index repositories, documentation, and research papers, then search across them with semantic search, deep research, and autonomous Oracle agents.

[![PyPI](https://img.shields.io/pypi/v/nia-ai-py)](https://pypi.org/project/nia-ai-py/)
[![Python](https://img.shields.io/pypi/pyversions/nia-ai-py)](https://pypi.org/project/nia-ai-py/)

## Installation

```bash
pip install nia-ai-py
```

Or with uv:

```bash
uv add nia-ai-py
```

Requires **Python 3.10+**.

## Quick Start

### High-Level SDK (Recommended)

```python
import os
from nia_py.sdk import NiaSDK

sdk = NiaSDK(api_key=os.environ["NIA_API_KEY"])

# Semantic search across all your indexed sources
results = sdk.search.universal(query="How does authentication work?")
print(results)
```

### Low-Level Client

For direct control over individual API calls:

```python
from nia_py import AuthenticatedClient
from nia_py.api.v2_api import search_universal_v2_v2_search_universal_post
from nia_py.models import UniversalSearchRequest

client = AuthenticatedClient(
    base_url="https://apigcp.trynia.ai/v2",
    token=os.environ["NIA_API_KEY"],
)

result = search_universal_v2_v2_search_universal_post.sync(
    client=client,
    body=UniversalSearchRequest(query="How does authentication work?"),
)
```

## SDK Reference

### NiaSDK

The main entry point. Initializes all sub-clients.

```python
sdk = NiaSDK(
    api_key="nia_...",                          # required
    base_url="https://apigcp.trynia.ai/v2",     # default
    timeout_seconds=60.0,                        # request timeout
    max_retries=2,                               # retries on 5xx / transport errors
    initial_backoff_seconds=0.5,                 # exponential backoff base
)
```

### SearchClient (`sdk.search`)

| Method | Description |
|--------|-------------|
| `query(messages, repositories, data_sources, **kwargs)` | Conversational search with chat history against specific sources |
| `universal(query, top_k, include_repos, include_docs, **kwargs)` | Semantic search across all indexed sources |
| `web(query, **kwargs)` | Web search |
| `deep(query, output_format, **kwargs)` | Multi-step research with AI analysis and citations |

```python
# Conversational search
result = sdk.search.query(
    messages=[{"role": "user", "content": "How does streaming work?"}],
    repositories=["vercel/ai"],
    include_sources=True,
    fast_mode=True,               # skip LLM for faster results
    reasoning_strategy="hybrid",  # vector, tree, or hybrid
)

# Universal search
result = sdk.search.universal(
    query="implement retry logic",
    top_k=20,
    include_repos=True,
    include_docs=True,
    alpha=0.7,                    # vector vs keyword weight
)

# Web search
result = sdk.search.web(query="latest LLM developments")

# Deep research
result = sdk.search.deep(
    query="Compare React Server Components vs traditional SSR",
    output_format="comparison table",
)
```

### SourcesClient (`sdk.sources`)

| Method | Description |
|--------|-------------|
| `create(payload)` | Create a new source (repo, docs, paper, etc.) |
| `list(type, query, status, category_id, limit, offset)` | List sources with filtering |
| `resolve(identifier, type)` | Resolve a source by name or URL |
| `get(source_id, type)` | Get source details by ID |
| `delete(source_id, type)` | Delete a source |

```python
# Index a repository
sdk.sources.create({"url": "https://github.com/vercel/ai"})

# Index documentation
sdk.sources.create({"url": "https://docs.anthropic.com", "display_name": "Anthropic Docs"})

# List repositories
repos = sdk.sources.list(type="repository", limit=50)

# Resolve by name
source = sdk.sources.resolve(identifier="vercel/ai")

# Delete
sdk.sources.delete(source_id="uuid-here")
```

**Source types:** `repository`, `documentation`, `research_paper`, `huggingface_dataset`, `local_folder`

### OracleClient (`sdk.oracle`)

| Method | Description |
|--------|-------------|
| `create_job(query, repositories, data_sources, output_format, model)` | Start an autonomous research job |
| `get_job(job_id)` | Get job status and result |
| `list_jobs(status, limit, skip)` | List your Oracle jobs |
| `wait_for_job(job_id, timeout_seconds, poll_interval_seconds)` | Poll until job completes |
| `stream_job_events(job_id)` | Stream SSE events from a running job |

```python
# Start a job
job = sdk.oracle.create_job(
    query="Analyze the caching architecture in Next.js",
    repositories=["vercel/next.js"],
    model="claude-sonnet-4-5-20250929",
)

# Wait for completion (default: 10 min timeout, 2s poll interval)
result = sdk.oracle.wait_for_job(job_id=job["id"])

# Or stream events in real-time
for event in sdk.oracle.stream_job_events(job_id=job["id"]):
    print(event)

# List completed jobs
completed = sdk.oracle.list_jobs(status="completed", limit=10)
```

**Available models:** `claude-opus-4-6`, `claude-opus-4-6-1m`, `claude-sonnet-4-5-20250929`, `claude-sonnet-4-5-1m`

## Low-Level API

Every API endpoint is a Python module with four functions:

```python
from nia_py.api.v2_api import index_repository_v2_v2_repositories_post
from nia_py.models import RepositoryRequest
from nia_py.types import Response

body = RepositoryRequest(repository="vercel/ai")

# Sync — returns parsed data or None
result = index_repository_v2_v2_repositories_post.sync(client=client, body=body)

# Sync detailed — returns Response[T] with status_code, headers, parsed
response: Response = index_repository_v2_v2_repositories_post.sync_detailed(client=client, body=body)

# Async
result = await index_repository_v2_v2_repositories_post.asyncio(client=client, body=body)

# Async detailed
response = await index_repository_v2_v2_repositories_post.asyncio_detailed(client=client, body=body)
```

### Key API Modules

Endpoints live under `nia_py.api.v2_api` and `nia_py.api.default`:

| Category | Key Endpoints |
|----------|--------------|
| **Search** | `unified_search_v2_v2_search_post`, `search_universal_v2_v2_search_universal_post`, `search_deep_v2_v2_search_deep_post`, `search_query_v2_v2_search_query_post` |
| **Repositories** | `index_repository_v2_v2_repositories_post`, `get_repository_tree_v2_v2_repositories_repository_id_tree_get`, `grep_repository_v2_v2_repositories_repository_id_grep_post` |
| **Data Sources** | `create_data_source_v2_v2_data_sources_post`, `list_data_sources_v2_v2_data_sources_get`, `grep_documentation_v2_v2_data_sources_source_id_grep_post` |
| **Sources** | `create_source_v2_sources_post`, `list_sources_v2_sources_get`, `resolve_source_v2_sources_resolve_get` |
| **Oracle** | `create_oracle_job_v2_oracle_jobs_post`, `get_oracle_job_v2_oracle_jobs_job_id_get`, `stream_oracle_job_v2_oracle_jobs_job_id_stream_get` |
| **Contexts** | `save_context_v2_v2_contexts_post`, `semantic_search_contexts_v2_v2_contexts_semantic_search_get` |
| **Package Search** | `package_search_hybrid_v2_v2_package_search_hybrid_post`, `package_search_grep_v2_v2_package_search_grep_post` |
| **GitHub** | `create_tracer_job_v2_github_tracer_post`, `github_code_search_v2_github_search_post` |

## Async Support

All endpoints support async via `asyncio` and `asyncio_detailed`:

```python
import asyncio
from nia_py.sdk import NiaSDK

sdk = NiaSDK(api_key="nia_...")

# The high-level SDK uses sync methods.
# For async, use the low-level client:
from nia_py import AuthenticatedClient
from nia_py.api.v2_api import search_universal_v2_v2_search_universal_post
from nia_py.models import UniversalSearchRequest

async def main():
    async with AuthenticatedClient(
        base_url="https://apigcp.trynia.ai/v2",
        token="nia_...",
    ) as client:
        result = await search_universal_v2_v2_search_universal_post.asyncio(
            client=client,
            body=UniversalSearchRequest(query="test"),
        )
        print(result)

asyncio.run(main())
```

## Error Handling

### High-Level SDK

```python
from nia_py.sdk import NiaSDK
from nia_py.sdk.errors import NiaSDKError, NiaAPIError, NiaTimeoutError

sdk = NiaSDK(api_key="nia_...")

try:
    result = sdk.search.universal(query="test")
except NiaAPIError as e:
    # API returned an error status (e.g., 401, 429)
    print(f"API error {e.status_code}: {e}")
except NiaTimeoutError as e:
    # Oracle job or long-running operation exceeded timeout
    print(f"Timeout: {e}")
except NiaSDKError as e:
    # Base class for all SDK errors
    print(f"SDK error: {e}")
```

### Low-Level Client

```python
from nia_py.errors import UnexpectedStatus

try:
    result = some_endpoint.sync(client=client, body=body)
except UnexpectedStatus as e:
    print(f"HTTP {e.status_code}: {e.content}")
```

### Retry Behavior

The SDK automatically retries on:
- **5xx server errors** — retried with exponential backoff
- **Transport/timeout errors** — retried with exponential backoff
- **4xx client errors** — raised immediately (not retried)

Backoff formula: `initial_backoff_seconds * 2^attempt`

## Client Configuration

```python
from nia_py import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://apigcp.trynia.ai/v2",
    token="nia_...",
    # Authentication
    prefix="Bearer",                    # token prefix (default)
    auth_header_name="Authorization",   # header name (default)
    # HTTP
    timeout=httpx.Timeout(60.0),        # request timeout
    verify_ssl=True,                    # SSL verification (True, False, or path to cert)
    follow_redirects=False,             # follow HTTP redirects
    raise_on_unexpected_status=False,   # raise on undocumented status codes
    # Custom
    headers={"X-Custom": "value"},      # additional headers
    cookies={"session": "abc"},         # cookies
    httpx_args={},                      # extra httpx.Client kwargs
)
```

### Context Manager

```python
with AuthenticatedClient(base_url="...", token="...") as client:
    result = some_endpoint.sync(client=client)

# Async
async with AuthenticatedClient(base_url="...", token="...") as client:
    result = await some_endpoint.asyncio(client=client)
```

## Documentation

- [SDK Quickstart](https://docs.trynia.ai/sdk/quickstart)
- [Authentication Guide](https://docs.trynia.ai/sdk/authentication)
- [Full Examples](https://docs.trynia.ai/sdk/examples)
- [REST API Reference](https://docs.trynia.ai/api-guide)

## License

MIT
