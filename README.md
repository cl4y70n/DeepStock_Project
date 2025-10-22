# **DeepStock — Previsão de Ações com Modelos Temporais**

## **Descrição do Projeto**

**DeepStock** é um sistema avançado de **previsão de preços de ações**, utilizando técnicas de **séries temporais clássicas e deep learning**.
O objetivo é gerar previsões precisas com base em dados históricos, avaliando tendências, volatilidade e indicadores técnicos, e comparar modelos clássicos (ARIMA, Prophet) com redes neurais (LSTM, GRU, Time Series Transformer) via **A/B testing**.

---

## **Arquitetura do Projeto**

```
DeepStock_Project/
│
├─ data/
│  ├─ raw/                  # Dados brutos (CSV, JSON)
│  ├─ processed/            # Dados limpos e feature-engineered
│  └─ features/             # Features extraídas (médias móveis, volatilidade)
│
├─ src/
│  ├─ data_loader/          # Carregamento de dados
│  │  └─ load_data.py
│  ├─ preprocessing/        # Limpeza e feature engineering
│  │  └─ feature_engineering.py
│  ├─ models/               # Modelos clássicos e deep learning
│  │  ├─ arima_model.py
│  │  ├─ prophet_model.py
│  │  ├─ lstm_model.py
│  │  └─ transformer_model.py
│  ├─ evaluation/           # Métricas e backtesting
│  │  └─ backtest.py
│  ├─ ab_testing/           # Comparação estatística de modelos
│  │  └─ ab_test.py
│  ├─ forecasting/          # Pipeline de previsão
│  │  └─ predict.py
│  ├─ utils/                # Funções auxiliares
│  │  └─ helpers.py
│  └─ dashboard/            # Dashboard Streamlit
│     └─ app.py
│
├─ notebooks/               # EDA e testes de modelos
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ params.yaml              # Hiperparâmetros e configs
└─ README.md
```

---

## **Tecnologias e Bibliotecas**

* **Python 3.10+**
* **Deep Learning:** PyTorch, TensorFlow, LSTM, GRU, Time Series Transformer
* **Forecasting Clássico:** ARIMA, Prophet
* **Data Handling:** Pandas, Numpy
* **Visualização:** Matplotlib, Seaborn, Plotly
* **Dashboard:** Streamlit
* **Deployment:** Docker, Docker Compose
* **MLOps:** MLflow (opcional)
* **Teste Estatístico:** scipy.stats para A/B testing

---

## **Funcionalidades**

1. Ingestão de dados históricos de ações.
2. Pré-processamento com limpeza, normalização e feature engineering.
3. Treinamento de modelos: ARIMA, Prophet, LSTM, GRU, Time Series Transformer.
4. Avaliação de modelos via métricas: RMSE, MAE, MAPE.
5. Backtesting para validar previsões.
6. A/B testing para comparar modelos clássicos e deep learning.
7. Pipeline de previsão automatizado para novos dados.
8. Dashboard interativo com gráficos e comparações.

---

## **Pipeline de Desenvolvimento**

1. **Coleta de dados**: CSV, Yahoo Finance ou Alpha Vantage.
2. **Pré-processamento**: limpeza, normalização e feature engineering.
3. **Treinamento de modelos**:

   * ARIMA e Prophet (séries clássicas)
   * LSTM, GRU, Time Series Transformer (deep learning)
4. **Avaliação e Backtesting**: métricas e comparação histórica.
5. **A/B Testing**: estatística para medir desempenho relativo.
6. **Pipeline de Previsão**: gerar previsões em batch ou real-time.
7. **Dashboard Streamlit**: visualização interativa.
8. **Deploy com Docker**: imagem pronta para execução em qualquer ambiente.

---

## **Como Rodar Localmente**

### 1. Clonar o repositório

```bash
git clone https://github.com/cl4y70n/deepstock-project.git
cd deepstock-project
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Colocar dados históricos

* CSVs em `data/raw/`

### 5. Executar exemplos mínimos

```bash
python src/data_loader/load_data.py
python src/preprocessing/feature_engineering.py
python src/models/lstm_model.py
python src/models/transformer_model.py
python src/models/arima_model.py
python src/models/prophet_model.py
```

### 6. Rodar Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## **Deploy com Docker**

1. Build da imagem:

```bash
docker build -t deepstock:latest .
```

2. Rodar via Docker Compose:

```bash
docker-compose up --build
```

3. Acesse o dashboard: `http://localhost:8501`

---

## **Contribuição**

1. Fork do repositório
2. Criar branch: `git checkout -b feature/nome-feature`
3. Commit: `git commit -m "Descrição da feature"`
4. Push: `git push origin feature/nome-feature`
5. Abrir Pull Request

---

## **Autor**

* **Clayton** – [GitHub](https://github.com/cl4y70n)

---

Quer que eu faça isso agora?
