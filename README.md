CoinGecko-Project/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── etl/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── prefect_flow.py
│
├── dbt/
│   ├── dbt_project.yml
│   ├── profiles.yml
│   └── models/
│       ├── sources.yml
│       ├── staging/
│       │   └── stg_crypto_prices.sql
│       ├── intermediate/
│       │   └── int_crypto_metrics.sql
│       └── marts/
│           ├── crypto_daily.sql
│           └── crypto_summary.sql
│
├── dashboard/
│   └── app.py
│
├── logs/
│   └── .gitkeep
│
└── scheduler/
    └── simple_orchestrator.py
