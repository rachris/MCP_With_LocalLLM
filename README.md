# Introduction

I am rather new in the field of the LLM's and learning about the Model Context Protocol looked an interesting topic to start with. 
And that fitted well with my Open Source aspiration and I have always kept an eye on Open Source Community and took part of Open Source events for the past 20 years. So combining this MCP protocol, although a protocol developped by Anthropic but shared to the Community as Open Source framework with an open weights LLM looked 
an interesting project. Also, from an enterprise point of view, the use of open weights LLM's would be quite interesting as it can be installed on premise and it keeps control of its data and not subject to token pricing by OpenAI or Anthropic when using Frontier models. 
Regarding the combination (LLM+MCP), we can use the reasoning capability of an LLM to access and analyse Enterprise data by connecting both through he MCP protocol.


# Pre-requisite

-I installed an Alibaba Qwen's LLM which could fit on my HP laptop with 8Gb NVIDIA VRAM running on Ubuntu 26.01. In consequence I installed Qwen2.5-Coder-7B which has 7.61 billion parameters (6.53B non-embedding), taking up around 4.7 GB to 5.5 GB when 4-bit quantized (Q4_K_M). As such, this model could fit entirely in the VRAM of my machine and no need to add some swap space.

-Installation of Ollama and pull qwen2.5-coder:7b
```
sudo apt install curl
curl -fsSL https://ollama.com/install.sh | sh
```
-
