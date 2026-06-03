# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sim, os arquivos foram povoados com mais informações a fim de enriquecer a base de conhecimento do agente.]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[Os JSON/CSV são carregados no início da sessão através de funções python onde são tratados e são incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Os dados são injetados no prompt através de uma F-String, depois de definidas as regras de prompt do agente.]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
"nome": "João Silva",
"idade": 32,
"profissao": "Analista de Sistemas",
"renda_mensal": 5000.0,
"perfil_investidor": "moderado",

{
"nome": "Tesouro Selic",
"categoria": "renda_fixa",
"risco": "baixo",
"rentabilidade": "100% da Selic",
"aporte_minimo": 30.0,
"indicado_para": "Reserva de emergência e iniciantes"
},

2025-09-15     chat                   CDB                      Cliente perguntou sobre rentabilidade e prazos       sim
2025-09-22 telefone       Problema no app                            Erro ao visualizar extrato foi corrigido       sim
2025-10-01     chat         Tesouro Selic    Cliente pediu explicação sobre o funcionamento do Tesouro Direto       sim
```
