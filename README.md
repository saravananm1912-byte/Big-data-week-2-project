# Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing

## 📌 Project Overview

The **Real-Time Parallel Log Aggregation Engine** is a Python-based distributed log processing system designed to collect, process, partition, and aggregate log data efficiently.

The system uses **custom socket communication** to transfer log data and applies a **parallel MapReduce-style architecture** to process large amounts of log information.

The project helps identify and count different types of log events such as:

- INFO
- WARNING
- ERROR

---

## 🎯 Objectives

The main objectives of this project are:

- To collect log data in real time.
- To transfer logs using socket programming.
- To process multiple log records in parallel.
- To divide data into different partitions.
- To aggregate log information efficiently.
- To demonstrate a simple distributed data-processing architecture.

---

## ⚙️ System Architecture

```text
              ┌─────────────────┐
              │  Socket Client  │
              └────────┬────────┘
                       │
                       │ Log Data
                       ▼
              ┌─────────────────┐
              │  Socket Server  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Mapper      │
              │  Extract Logs   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Partitioner   │
              │ Divide the Data │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Reducer     │
              │ Aggregate Logs  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Final Results  │
              └─────────────────┘
