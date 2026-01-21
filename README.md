# 📋 Trabalho – Programação Dinâmica

**Disciplina:** Projeto e Análise de Algoritmos  
**Professor:** Raí Araújo de Miranda  
**Curso:** Sistemas de Informação  
**Período:** 5º  
**Ano/Semestre:** 2025.4  
**Instituição:** Universidade Federal do Piauí – UFPI  
**Campus:** Senador Helvídio Nunes de Barros – Picos  

---

## 👥 Equipe

| Nome | Responsabilidade |
|------|------------------|
| Luciano Sousa Barbosa | Implementação / Análise |
| Pedro Henrique Silva Rodrigues | Implementação / Análise |
| Tiago Lima de Moura | Implementação / Análise |

> Todos os integrantes participam da implementação, redação do trabalho e apresentação.

---

## 🎯 Objetivo do Trabalho

Este trabalho tem como objetivo analisar comparativamente algoritmos resolvidos por **Programação Dinâmica (PD)** e por **abordagem recursiva**, avaliando o impacto dessas técnicas no **tempo de execução** e no **consumo de memória**.

Busca-se demonstrar, de forma teórica e experimental, por que a Programação Dinâmica tende a ser mais eficiente que soluções recursivas ingênuas, especialmente em problemas com **subestrutura ótima** e **subproblemas sobrepostos**.

---

## 🧠 Tema Sorteado

**Algoritmo:** *Corte de Hastes*  
**Técnica Comparada:**  
- Versão Recursiva  
- Versão com Programação Dinâmica  

---

## 💻 Ambiente de Desenvolvimento

| Item | Especificação |
|------|---------------|
| **Linguagem** | C |
| **Sistema Operacional** | Windows 11 (Executado no Ubuntu 24.04.3 LTS via WSL2) |
| **Hardware** | Intel Core i5-12450H (12ª Gen, 8 núcleos, 12 threads, 2.00 GHz), 16 GB RAM |
| **Editor/IDE** | Visual Studio Code |
| **Ferramentas Auxiliares** | Python (análise e geração de gráficos) |

---

## 🧩 Descrição do Problema

O problema do **Corte de Hastes** consiste em determinar a melhor forma de cortar uma haste de comprimento `n`, de modo que a soma dos valores obtidos com os pedaços seja máxima, dado um vetor de preços para cada comprimento possível.

Esse problema apresenta:
- **Subestrutura ótima**
- **Subproblemas sobrepostos**

tornando-o ideal para análise com Programação Dinâmica.

---

## 🧪 Metodologia Experimental

### 🔹 Implementações
- Implementação **recursiva pura**, sem memorização
- Implementação com **Programação Dinâmica**, utilizando abordagem bottom-up

Ambas foram desenvolvidas **na mesma linguagem**, conforme exigido.

### 🔹 Cenários de Teste
Foram definidos múltiplos tamanhos de entrada, variando o comprimento da haste, garantindo:
- Mesmo conjunto de testes para ambas as versões
- Execução repetida para maior confiabilidade dos resultados

### 🔹 Métricas Avaliadas
- ⏱️ **Tempo de execução**
- 💾 **Consumo de memória**
- 📈 Escalabilidade conforme aumento do tamanho da entrada

---

## 📊 Resultados e Análise

- Tabelas comparativas de tempo e memória
- Gráficos:
  - Tempo × Tamanho da Entrada
  - Memória × Tamanho da Entrada
- Discussão detalhada sobre:
  - Diferença de desempenho entre as abordagens
  - Impacto da recomputação de subproblemas na versão recursiva
  - Vantagens da Programação Dinâmica

---

## 📝 Estrutura do Trabalho Escrito

- **Introdução**  
  Contextualização, motivação e definição do problema

- **Metodologia**  
  Descrição detalhada das versões:
  - Solução Recursiva
  - Solução com Programação Dinâmica  
  Processo de geração de dados e execução dos testes

- **Resultados**  
  Tabelas, gráficos e análise crítica dos resultados

- **Conclusão**  
  Discussão sobre eficiência e aplicabilidade da Programação Dinâmica

- **Referências**  
  Livros, artigos e materiais utilizados

---

## 🎤 Apresentação

- Duração: **20 a 30 minutos**
- Todos os integrantes participam
- Conteúdo abordado:
  - Explicação dos algoritmos
  - Demonstração passo a passo com exemplo pequeno
  - Apresentação dos resultados experimentais

---

## 📁 Estrutura do Projeto


---

## ✅ Checklist de Progresso

x -> para marcar

### 🔧 Implementação
- [x] Escolha do algoritmo
- [ ] Implementação recursiva
- [ ] Implementação com Programação Dinâmica
- [ ] Organização e documentação do código

### 🧪 Testes
- [ ] Definição dos cenários de teste
- [ ] Definição das métricas de análise
- [ ] Execução comparativa
- [ ] Coleta de métricas

### 📊 Análise
- [ ] Criação de tabelas
- [ ] Geração de gráficos
- [ ] Análise crítica dos resultados

### 📝 Entregas
- [ ] Trabalho escrito
- [ ] Slides
- [ ] Apresentação oral

---

## 📌 Critérios de Avaliação

- **Apresentação (50%)**
  - Clareza, organização, domínio do conteúdo e gestão do tempo

- **Trabalho escrito e implementação (50%)**
  - Profundidade da análise
  - Organização do texto
  - Qualidade e clareza do código

---

## 🔗 Links

- 📄 Relatório: *(https://www.overleaf.com/project/696cf1c01d50337624794b98)*  
- 📊 Slides: *(https://docs.google.com/presentation/d/1ugzm7Y4NWLEIF5hORTJkRCAgyBZvtYg2S5923zM5vDI/edit?usp=sharing)*  
- 💻 Repositório: *(https://github.com/phsrod/Trabalho02-PAA)*  

---

**📌 Última atualização:** 18/01/2025  
