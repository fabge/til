# tools

[What if you don't need MCP?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)

MCP servers for browser dev tools often provide 20+ tools consuming 13-18k tokens (6-9% of context), covering all bases but confusing agents and lacking composability.

A simpler approach: give agents minimal Bash/Node.js scripts that leverage their existing knowledge. The author's browser tools (start, navigate, eval JS, screenshot, pick elements) use just 225 tokens in a README.

Benefits: context efficiency, composability (chain commands, pipe outputs), easy extensibility (add/modify tools in minutes), and works with any coding agent.

Bash and code are composable; MCP results must flow through agent context. For many use cases, simple CLI tools that agents can invoke and extend are more efficient than rigid MCP server structures.
