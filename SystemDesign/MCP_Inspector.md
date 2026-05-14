# MCP Inspector Note
* 主要是放置一些在執行 ChatGPT Task Scheduler 作為 Practice 的一些 Note

1. MCP Inspector 一開始進行 initialize
2. 然後會 list tools (找出目前 MCP Server 有哪些工具可使用)
```json
Request
{
  "method": "tools/list",
  "params": {}
}

Response
{
  "tools": [
    {
      "name": "task.create",
      "description": "Schedule a new task for future execution",
      "inputSchema": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "What the task should do"
          },
          "scheduled_at": {
            "type": "string",
            "format": "date-time",
            "description": "When to run, ISO 8601 format (e.g. 2026-05-03T10:00:00)"
          }
        },
        "required": [
          "description",
          "scheduled_at"
        ]
      }
    },
    {
      "name": "task.list",
      "description": "List all scheduled tasks",
      "inputSchema": {
        "type": "object",
        "properties": {}
      }
    },
    {
      "name": "task.status",
      "description": "Get the status of a scheduled task by job_id",
      "inputSchema": {
        "type": "object",
        "properties": {
          "job_id": {
            "type": "integer",
            "description": "The job ID returned by task.create"
          }
        },
        "required": [
          "job_id"
        ]
      }
    },
    {
      "name": "task.cancel",
      "description": "Cancel a scheduled task that hasn't completed yet",
      "inputSchema": {
        "type": "object",
        "properties": {
          "job_id": {
            "type": "integer",
            "description": "The job ID to cancel"
          }
        },
        "required": [
          "job_id"
        ]
      }
    }
  ]
}
```
3. 然後開始 Call 工具
```json
Request
{
  "method": "tools/call",
  "params": {
    "name": "task.create",
    "arguments": {
      "description": "Summarize tech news",
      "scheduled_at": "2025-01-01T00:00:00"
    },
    "_meta": {
      "progressToken": 0
    }
  }
}

Response
{
  "content": [
    {
      "type": "text",
      "text": "{\"job_id\": 1, \"status\": \"pending\", \"scheduled_at\": \"2025-01-01 00:00:00\"}"
    }
  ],
  "isError": false
}
```