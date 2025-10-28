import json
import csv
import os
from web3 import Web3
from solders.keypair import Keypair
from eth_account import Account
from mnemonic import Mnemonic  # 新增助记词库

# 初始化助记词生成器
mnemo = Mnemonic("english")
# 启用EVM钱包助记词功能（解决AttributeError问题）
Account.enable_unaudited_hdwallet_features()


def generate_evm_wallet():
    """生成EVM兼容钱包（助记词+私钥+地址）"""
    # 生成12词助记词
    mnemonic = mnemo.generate(strength=128)
    # 通过助记词推导私钥
    private_key = Account.from_mnemonic(mnemonic).key.hex()
    # 获取地址
    address = Account.from_key(private_key).address
    return {
        "mnemonic": mnemonic,
        "private_key": private_key,
        "address": address
    }


def generate_solana_wallet():
    """生成Solana钱包（助记词+私钥+地址）"""
    # 生成12词助记词
    mnemonic = mnemo.generate(strength=128)
    # 通过助记词推导私钥（Solana使用BIP39标准）
    seed = mnemo.to_seed(mnemonic)
    keypair = Keypair.from_seed(seed[:32])  # Solana私钥为32字节
    private_key = list(keypair.secret_key)
    address = str(keypair.pubkey())
    return {
        "mnemonic": mnemonic,
        "private_key": private_key,
        "address": address
    }


def save_to_json(data, filename):
    """保存数据到JSON文件"""
    with open(f"{filename}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"已保存JSON文件: {filename}.json")


def save_to_csv(data, filename, wallet_type):
    """保存数据到CSV文件"""
    with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # 写入表头（新增mnemonic列）
        writer.writerow(["index", "mnemonic", "private_key", "address"])
        # 写入数据
        for i, item in enumerate(data, 1):
            priv_key = item["private_key"] if wallet_type == "evm" else str(item["private_key"])
            writer.writerow([i, item["mnemonic"], priv_key, item["address"]])
    print(f"已保存CSV文件: {filename}.csv")


def main():
    print("=== 区块链钱包生成工具（含助记词版）===")

    # 1. 选择钱包类型
    while True:
        choice = input("\n请选择要生成的钱包类型:\n1. EVM (以太坊、BSC等兼容链)\n2. Solana\n请输入数字(1/2): ").strip()
        if choice in ["1", "2"]:
            wallet_type = "evm" if choice == "1" else "solana"
            break
        print("输入无效，请重新选择！")

    # 2. 选择保存格式
    while True:
        fmt_choice = input("\n请选择保存格式:\n1. JSON\n2. CSV\n3. 同时保存两者\n请输入数字(1/2/3): ").strip()
        if fmt_choice in ["1", "2", "3"]:
            save_formats = []
            if fmt_choice in ["1", "3"]:
                save_formats.append("json")
            if fmt_choice in ["2", "3"]:
                save_formats.append("csv")
            break
        print("输入无效，请重新选择！")

    # 3. 输入生成数量
    while True:
        try:
            count = input("\n请输入要生成的钱包数量: ").strip()
            count = int(count)
            if count > 0:
                break
            print("数量必须大于0，请重新输入！")
        except ValueError:
            print("请输入有效的数字！")

    # 4. 输入保存文件名
    while True:
        filename = input("\n请输入保存的文件名(无需后缀): ").strip()
        if filename:
            # 检查文件是否已存在
            existing_files = []
            for fmt in save_formats:
                if os.path.exists(f"{filename}.{fmt}"):
                    existing_files.append(f"{filename}.{fmt}")
            if existing_files:
                overwrite = input(f"文件 {', '.join(existing_files)} 已存在，是否覆盖? (y/n): ").strip().lower()
                if overwrite == "y":
                    break
            else:
                break
        print("文件名不能为空，请重新输入！")

    # 生成钱包
    print(f"\n正在生成{count}个{wallet_type.upper()}钱包...")
    wallets = []
    generator = generate_evm_wallet if wallet_type == "evm" else generate_solana_wallet
    for _ in range(count):
        wallets.append(generator())

    # 保存文件
    for fmt in save_formats:
        if fmt == "json":
            save_to_json(wallets, filename)
        else:
            save_to_csv(wallets, filename, wallet_type)

    print("\n操作完成！")


if __name__ == "__main__":
    main()
