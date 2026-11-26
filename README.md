# Introduction

I am rather new in the field of the LLM's and learning about the Model Context Protocol looked interesting to me. 
I have always been a fervent promoter of Open Source tools so integrating the MCP, although a protocol developped by Anthropic but shared to the Community as Open Source framework and an open weights LLM looked 
an interesting project. Also, from an enterprise point of view, it would be more re-assuring to use open weights LLM which could be on premise, ensuring that the data is not sent on third-party server.
Combined the reasoning capability of the LLM with the MCP protocol, the enterprise data could be accessed and analysed by the LLM in a secured manner.

# Pre-requisite

-I installed an Alibaba Qwen's LLM which could fit on my HP laptop with 8Gb NVIDIA VRAM. In consequence I installed Qwen2.5-Coder-7B which has 7.61 billion parameters (6.53B non-embedding), taking up around 4.7 GB to 5.5 GB when 4-bit quantized (Q4_K_M). As such, this model could fit entirely in the VRAM of my machine and no need to add some swap space.

-Installation of Ollama and pull qwen2.5-coder:7b
```
sudo apt install curl
curl -fsSL https://ollama.com/install.sh | sh
```
-
