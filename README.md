# 📌 Projeto da Disciplina de Teoria dos Grafos

## Disciplina: Teoria dos Grafos 📚
### Curso: Ciência da Computação 💻
### Universidade: Ufersa - Universidade Federal Rural do Semi-Árido 🌱
### Unidade Responsável: Departamento de Computação 🏛️
### Modalidade: Presencial 🏫
### Ano-Período: 2025 📅

## 📖 Sumário
1. [Introdução](#introducao)
2. [Objetivos](#objetivos)
3. [Conteúdo Programático](#conteudo-programatico)
4. [Competências e Habilidades](#competencias-habilidades)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Algoritmo de Busca em Largura (BFS)](#algoritmo-bfs)
7. [Referências Bibliográficas](#referencias-bibliograficas)

---

## 📚 Introdução <a id="introducao"></a>
Esta disciplina tem como objetivo apresentar os conceitos básicos de Teoria dos Grafos, explorando a modelagem e a resolução de problemas computacionais utilizando diferentes representações de grafos.

## 🎯 Objetivos <a id="objetivos"></a>
- Introduzir os conceitos fundamentais da Teoria dos Grafos.
- Estudar e implementar algoritmos em grafos.
- Modelar e resolver problemas utilizando grafos.
- Compreender a aplicabilidade dos grafos em diferentes contextos computacionais.

## 📌 Conteúdo Programático <a id="conteudo-programatico"></a>

### Unidade I - Introdução e Conceitos Básicos de Grafos (20h)
- Apresentação da disciplina, plano de curso e metodologia de ensino.
- Definições fundamentais: vértices, arestas, caminhos e ciclos.
- Grafos bipartidos, rotulados e valorados.
- Grafos Eulerianos e Hamiltonianos.
- **Algoritmo de Busca em Largura (BFS) e sua aplicação**.

### Unidade II - Representação de Grafos e Algoritmos de Caminho Mínimo (20h)
- Representação por matriz de adjacência e lista de adjacência.
- Estruturas de dados para manipulação de grafos.
- Árvores e florestas, árvore geradora mínima.
- Algoritmos de busca: busca em largura (BFS) e busca em profundidade (DFS).
- Algoritmos de caminho mínimo: Dijkstra e Bellman-Ford.

### Unidade III - Fluxo em Redes e Problemas em Grafos (20h)
- Conceitos de fluxo em redes.
- Algoritmos de fluxo máximo: Ford-Fulkerson.
- Algoritmos de fluxo a custo mínimo: Busacker & Gowen.
- Ordenação topológica.
- Problemas de coloração de grafos.

## 🏆 Competências e Habilidades <a id="competencias-habilidades"></a>
- Compreender os conceitos básicos da Teoria dos Grafos.
- Identificar problemas computacionais que podem ser resolvidos utilizando grafos.
- Implementar algoritmos de grafos e avaliar sua eficiência.
- Aplicar a Teoria dos Grafos para resolver problemas práticos em computação.

## 📂 Estrutura do Projeto <a id="estrutura-do-projeto"></a>
A estrutura do projeto atual está organizada da seguinte forma:

```
Teoria_Dos_Grafos/
│── README.md
│── Algoritmo BFS/
│   │── arvore_bfs.png
│   │── BreadthFirstSearch.py
│   │── caminho_mais_curto.png
│   │── grafo_original.png
```

- **README.md**: Documento com informações gerais do projeto.
- **Algoritmo BFS/**: Contém a implementação do algoritmo de busca em largura (BFS) e imagens geradas pelo código.

## 🔍 Algoritmo de Busca em Largura (BFS) <a id="algoritmo-bfs"></a>
O algoritmo de **Busca em Largura (BFS)** é um dos principais algoritmos para percorrer grafos, sendo utilizado para encontrar caminhos mínimos em grafos não ponderados.

### 🔹 Funcionamento do BFS:
1. Começa a partir de um nó inicial e o marca como visitado.
2. Explora todos os seus vértices vizinhos antes de avançar para os próximos nós.
3. Utiliza uma **fila** para garantir a exploração em camadas.
4. Retorna uma **árvore de busca** e um **caminho mínimo** entre o nó inicial e um destino.

### 🔹 Implementação em Python:
O projeto inclui um código em Python que:
- Representa um grafo por matriz de adjacência.
- Utiliza a biblioteca `networkx` para visualização.
- Implementa o BFS para gerar uma árvore de busca e encontrar o caminho mais curto.
- Gera e salva imagens do grafo original, da árvore BFS e do caminho mais curto.

### 🔹 Exemplos de Saída:
- **grafo_original.png**: Representação visual do grafo antes da busca.
- **arvore_bfs.png**: Exibe a árvore gerada pelo BFS.
- **caminho_mais_curto.png**: Destaca o menor caminho encontrado pelo algoritmo.

## 📚 Referências Bibliográficas <a id="referencias-bibliograficas"></a>

### 📖 Obrigatórias:
1. Goldbarg, Marco. *Grafos: conceitos, algoritmos e aplicações*. Elsevier, 2012.
2. Boaventura, Paulo Osvaldo. *Grafos: teoria, modelos e algoritmos*. Edgard Blucher, 2006.
3. West, Douglas B. *Introduction to Graph Theory*. 2ª ed. Prentice-Hall, 2000.

### 📚 Complementares:
1. Szwarcfiter, J. L. *Grafos e algoritmos computacionais*. Editora Campus, 1984.
2. Cardoso, Domingos Moreira. *Matemática discreta, combinatória, teoria dos grafos, algoritmos*. Editora Escolar, Lisboa, 2009.
3. Bondy, J. A., Murty, U. S. R. *Graph Theory*. Springer, 2008.

---
Este documento descreve a ementa, metodologia e objetivos da disciplina de Teoria dos Grafos, fornecendo um guia detalhado para os alunos acompanharem o curso e o projeto prático relacionado.
