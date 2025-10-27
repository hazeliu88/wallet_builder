# 区块链钱包生成工具

一款支持生成EVM兼容链与Solana钱包的Python工具，可自定义生成数量并导出为JSON/CSV格式，本地运行保障私钥安全。

## ✨ 功能特性

- 支持两种钱包类型：EVM（以太坊、BSC、Polygon等）和Solana

- 灵活的文件导出：可选JSON、CSV或同时导出两种格式

- 自定义配置：可指定钱包生成数量和输出文件名

- 安全保障：本地生成私钥，无网络传输，避免信息泄露

- 用户友好：交互式命令行界面，引导式操作流程

## 📋 环境准备

### 1. 依赖库安装

克隆仓库后，执行以下命令安装所需依赖：

```bash

pip install -r requirements.txt
```

### 2. 依赖说明

|库名|用途|
|---|---|
|web3|EVM链钱包生成基础库|
|eth-account|EVM账户私钥与地址生成|
|solders|Solana钱包 keypair 生成|
## 🚀 使用步骤

1. **克隆仓库**：

2. **安装依赖**：执行 `pip install -r requirements.txt`

3. **运行程序**：

4. **交互式操作**：
        选择钱包类型（1.EVM / 2.Solana）

5. 选择保存格式（1.JSON / 2.CSV / 3.两者都要）

6. 输入生成钱包数量（需大于0）

7. 输入输出文件名（无需后缀）

8. **查看结果**：生成的文件会保存在项目根目录下

## 📁 文件说明

- `wallet_builder.py`：主程序文件，包含钱包生成与文件保存逻辑

- `requirements.txt`：项目依赖列表

- `.gitignore`：Git忽略规则，防止提交私钥文件与冗余文件

- `README.md`：项目说明文档（本文档）

## 📊 输出格式示例

### JSON格式

```json

[
  {
    "private_key": "0xabc123...",
    "address": "0xDef456..."
  },
  {
    "private_key": "0x789xyz...",
    "address": "0xAaBbCc..."
  }
]
```

### CSV格式

```Plain Text

index,private_key,address
1,0xabc123...,0xDef456...
2,0x789xyz...,0xAaBbCc...
```
