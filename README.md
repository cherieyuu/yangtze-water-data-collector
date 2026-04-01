# yangtze-water-data-collector

Live Demo: [https://water.cherie16.com.cn/](https://water.cherie16.com.cn/)

A Scrapy-based data collection service for a hydrology visualization platform.
It collects public hydrology station data, normalizes the records, and stores them in MongoDB for downstream API and dashboard use.

This repository contains the data collection service for a hydrology visualization platform, working with a frontend dashboard and a backend API service.

Platform components:
- Frontend: [yangtze-water-dashboard](https://github.com/cherieyuu/yangtze-water-dashboard)
- Backend API: [yangtze-water-api](https://github.com/cherieyuu/yangtze-water-api)
- Data collection: [yangtze-water-data-collector](https://github.com/cherieyuu/yangtze-water-data-collector)

## Features

- Scrapy-based station data collection
- MongoDB storage pipeline
- Environment-variable based configuration
- Basic invalid-data filtering before persistence
- Upsert-based write strategy to reduce duplicate records
- Integration-ready output for the backend API service

## Tech Stack

- Python 3
- Scrapy 2
- PyMongo 3
- lxml 4
- MongoDB

## Project Structure

```text
scrapy.cfg
waterDataScrapy/
  items.py            item definitions
  middlewares.py      Scrapy middleware hooks
  pipelines.py        MongoDB pipeline and data cleaning
  settings.py         scraper settings and env loading
  spiders/
    main_water.py     main spider
requirements.txt      Python dependencies
```

## Getting Started

### Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure environment variables

Create a local `.env` file based on `.env.example`.

Example:

```bash
cp .env.example .env
```

### Run the spider

```bash
scrapy crawl main_water
```

## Data Flow

A typical data flow is:

```text
yangtze-water-data-collector -> MongoDB -> yangtze-water-api -> yangtze-water-dashboard
```

The collector is responsible for gathering source data and writing normalized records into MongoDB, where they can be consumed by the API service.

## Deployment Notes

When running in different environments, update the Mongo-related environment variables accordingly.

Examples:

```text
MONGODB_HOST=localhost:27017
```

or in Docker networks:

```text
MONGODB_HOST=mongodb:27017
```

## Data and Compliance Notice

This project is for personal learning and technical research only.
It is intended to practice data collection, data cleaning, and system integration workflows.

Please note:
- do not use third-party collected data for commercial purposes

## License

MIT

---

# yangtze-water-data-collector

线上地址：[https://water.cherie16.com.cn/](https://water.cherie16.com.cn/)

一个基于 Scrapy 的数据采集服务，用于支撑水文可视化平台。
它负责采集公开水文站点数据、规范化记录，并将结果写入 MongoDB，供后续 API 服务和前端大屏使用。

这个仓库是一个水文可视化平台的数据采集服务，配合前端大屏和后端 API 服务共同运行。

平台组成：
- 前端：[yangtze-water-dashboard](https://github.com/cherieyuu/yangtze-water-dashboard)
- 后端接口：[yangtze-water-api](https://github.com/cherieyuu/yangtze-water-api)
- 数据采集：[yangtze-water-data-collector](https://github.com/cherieyuu/yangtze-water-data-collector)

## 功能特性

- 基于 Scrapy 的站点数据采集
- MongoDB 存储流水线
- 基于环境变量的配置方式
- 入库前的基础异常数据过滤
- 基于 upsert 的写入策略，减少重复记录
- 为后端 API 服务提供可直接对接的数据输出

## 技术栈

- Python 3
- Scrapy 2
- PyMongo 3
- lxml 4
- MongoDB

## 项目结构

```text
scrapy.cfg
waterDataScrapy/
  items.py            数据项定义
  middlewares.py      Scrapy 中间件钩子
  pipelines.py        MongoDB 流水线与数据清洗
  settings.py         爬虫配置与环境变量读取
  spiders/
    main_water.py     主爬虫
requirements.txt      Python 依赖
```

## 本地启动

### 安装依赖

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 配置环境变量

基于 `.env.example` 创建本地 `.env` 文件。

例如：

```bash
cp .env.example .env
```

### 运行爬虫

```bash
scrapy crawl main_water
```

## 数据流说明

一个典型的数据流如下：

```text
yangtze-water-data-collector -> MongoDB -> yangtze-water-api -> yangtze-water-dashboard
```

采集服务负责抓取源数据并将规范化后的记录写入 MongoDB，随后由 API 服务读取并提供给前端大屏使用。

## 部署说明

在不同运行环境中，请根据实际情况调整 Mongo 相关环境变量。

例如本机运行：

```text
MONGODB_HOST=localhost:27017
```

或者在 Docker 网络中运行：

```text
MONGODB_HOST=mongodb:27017
```

## 数据与合规说明

本项目仅用于个人学习和技术研究。
主要用于练习数据采集、数据清洗和系统集成流程。

请注意：
- 不要将第三方采集数据用于商业用途

## License

MIT
