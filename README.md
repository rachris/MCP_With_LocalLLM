# Introduction

I am rather new in the field of the LLM's and learning about the Model Context Protocol looked an interesting topic to start with. 
And that fitted well with my Open Source aspiration and I have always kept an eye on Open Source Community and took part of Open Source events for the past 20 years. So combining this MCP protocol, although a protocol developped by Anthropic but shared to the Community as Open Source framework with an open weights LLM looked 
an interesting project. Also, from an enterprise point of view, the use of open weights LLM's would be quite interesting as it can be installed on premise and it keeps control of its data and not subject to token pricing by OpenAI or Anthropic when using Frontier models. 
Regarding the combination (LLM+MCP), we can use the reasoning capability of an LLM to access and analyse Enterprise data by connecting both through he MCP protocol.

We propose here to build a rather simple setup: 

The setup is rather simple: we will ask the LLM to make a summary content of a given website but within the setup of the MCP protocol. That will require defining a MCP-Server and a MCP-Client. In short, the user is making a request to the MCP-Client, which will submit this request to the LLM. The MCP-Server has already provided a list of tools available to the LLM and depending on the request of the user, the LLM will decide if he can answer using its own reasoning or if it requires a call to one of the tools the MCP-Server has available. Because the tools are deterministic, the information the LLM has been given by the MPC-Server about the tools should help him make a call to the tools with the correct arguments.


# Quick introduction to MCP




# Pre-requisite

-I installed an Alibaba Qwen's LLM which could fit on my HP laptop with 8Gb NVIDIA VRAM running on Ubuntu 26.01. In consequence I installed Qwen2.5-Coder-7B which has 7.61 billion parameters (6.53B non-embedding), taking up around 4.7 GB to 5.5 GB when 4-bit quantized (Q4_K_M). As such, this model could fit entirely in the VRAM of my machine with no need to add some swap space.

-Installation of Ollama and pull qwen2.5-coder:7b
```
sudo apt install curl
curl -fsSL https://ollama.com/install.sh | sh
```


-
