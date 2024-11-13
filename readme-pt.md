# Transferência de Aprendizado com Dados de Áudio - TCC

Este projeto foi elaborado durante meu trabalho de conclusão de curso e visou investigar a aplicação de **transferência de aprendizado** para classificação de emoções em áudios, utilizando redes neurais pré-treinadas como **YAMNet** e **VGGish**. O objetivo é comparar o desempenho de diferentes classificadores, como **SVM**, **Random Forest**, **Naive Bayes** e **MLP**, ao classificar emoções a partir de dados de áudio.

O conjunto de dados utilizado é o **RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)**, amplamente utilizado para análise de emoções em áudio. Você pode acessar o conjunto de dados RAVDESS no [link](https://zenodo.org/records/1188976).

> **Note**: If you prefer, you can also read the project description in English 🇺🇸. Please refer to the [README in english](readme.md) for more details.

## 🗂️ Índice

-   [Descrição](#descrição)
-   [Tecnologias](#tecnologias)
-   [Pré-requisitos](#pré-requisitos)
-   [Instalação](#instalação)
-   [Como Usar](#como-usar)
-   [Licença](#licença)

## 📜 Descrição

Este projeto aplica **transferência de aprendizado** usando redes neurais pré-treinadas (**YAMNet** e **VGGish**) para extrair características de áudio. Em seguida, treinamos classificadores tradicionais (**SVM**, **Random Forest**, **Naive Bayes** e **MLP**) sobre essas características extraídas, assim como características derivadas de **espectrogramas de Mel**, a fim de classificar emoções nos áudios.

O fluxo do projeto é o seguinte:

1. **Extração de características**:

    - **VGGish**: Utiliza um modelo pré-treinado para extrair características de áudio.
    - **YAMNet**: Baseado em um modelo de rede neural para extração de características de áudio.
    - **Espectrogramas de Mel**: Extração de espectrogramas de Mel diretamente dos arquivos de áudio.

2. **Treinamento de Classificadores**:
    - Treinamento de **SVM**, **Random Forest**, **Naive Bayes** e **MLP** para classificar as emoções a partir das características extraídas.

> **Importante**: O script `generate_csv_metadata.py` espera que os arquivos de áudio estejam em uma pasta chamada `data`. Ele trabalha apenas com os arquivos de **áudio (não inclui os áudios dos atores cantando nem os arquivos de vídeo)**. Certifique-se de colocar apenas os arquivos de áudio de fala na pasta `data` para o script funcionar corretamente. Ou modificar o script, se você preferir fazer de uma maneira diferente.

## 💻 Tecnologias

Este projeto foi desenvolvido utilizando

as seguintes bibliotecas e ferramentas:

-   **Python 3.11**
-   **Jupyter Notebooks** (para análise interativa)
-   **Pandas (v 2.2.1)**: Para análise e manipulação de dados
-   **Librosa (v 0.10.1)**: Para processamento de arquivos de áudio
-   **TensorFlow (v 2.13.0)**: Para criação e adaptação de redes neurais
-   **TensorFlow Hub (v 0.16.1)**: Para acesso a modelos pré-treinados de aprendizado de máquina
-   **Scikit-learn (v 1.4.1.post1)**: Para treinamento de modelos de aprendizado de máquina tradicionais
-   **Matplotlib (v 3.8.3)**: Para visualização de resultados e gráficos

## 📌 Pré-requisitos

Este projeto foi desenvolvido utilizando **Python 3.11** e requer as seguintes bibliotecas:

-   **Pandas** para manipulação de dados
-   **Librosa** para leitura e processamento de arquivos de áudio
-   **TensorFlow** e **TensorFlow Hub** para redes neurais e transferência de aprendizado
-   **Scikit-learn** para criação de modelos de aprendizado de máquina
-   **Matplotlib** para visualização de resultados

Um arquivo `requirements.txt` com todas as dependências pode ser encontrado no repositório.

## 🛠️ Instalação

Para rodar este projeto, siga as instruções abaixo:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

Ative o ambiente:

-   No Windows:

    ```bash
    venv\Scripts\activate
    ```

-   No Mac/Linux:
    ```bash
    source venv/bin/activate
    ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 🧑🏽‍💻 Como Usar

### Passo 1: Gerar a tabela CSV com os caminhos dos arquivos e suas emoções

Execute o script `generate_csv_metadata.py` para gerar um arquivo CSV contendo os caminhos dos arquivos de áudio e as emoções que eles representam. Este arquivo será utilizado para extração das características nos notebooks.

> **Importante**: O script `generate_csv_metadata.py` espera que os arquivos de áudio estejam localizados em uma pasta chamada `data`. Ele só processa arquivos de **áudio (não inclui os áudios de atores cantando nem arquivos de vídeo)**. Coloque apenas os arquivos de áudio de fala na pasta `data` para o script funcionar corretamente.

```bash
python generate_csv_metadata.py
```

### Passo 2: Extração de Características

Após gerar o CSV, você pode usar os notebooks Jupyter para extrair as características dos áudios. Os notebooks estão organizados da seguinte forma:

1. **YAMNet**:

    - Abra o notebook `yamnet_feature_extraction.ipynb` para extrair características usando o modelo YAMNet.

2. **VGGish**:

    - Abra o notebook `vggish_feature_extraction.ipynb` para extrair características usando o modelo VGGish.

3. **Espectrogramas de Mel**:
    - Abra o notebook `mel_spectrogram_extraction.ipynb` para extrair espectrogramas de Mel a partir dos áudios.

### Passo 3: Treinamento dos Classificadores

Depois de extrair as características, você pode treinar os classificadores usando as features extraídas. O código para isso está nos notebooks, onde você pode treinar **SVM**, **Random Forest**, **Naive Bayes** e **MLP** para prever a emoção nos áudios.

## 🔓 Licença

Este projeto está licenciado sob a **Licença Pública Geral GNU (GPL v3)**. Isso significa que você é livre para usar, modificar e distribuir este código, desde que também o compartilhe sob a mesma licença. Ou seja, qualquer trabalho derivado também precisa ser aberto e licenciado sob a **GPL v3**.

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
