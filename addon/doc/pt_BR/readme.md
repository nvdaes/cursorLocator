# Cursor Locator #

* Autores: Noelia Ruiz Martínez, Sergio Gómez Codina.

Esse complemento permite saber a posição do cursor do sistema em relação ao
início da linha atual, enquanto se digita para adicionar texto em documentos
ou controles de várias linhas.

Esse recurso depende da aparência visual dos aplicativos. Portanto, talvez
seja necessário desativar o ajuste de linha ou configurar o complemento para
programas diferentes.

## Configurações do localizador de cursor ##

Esse painel está disponível no menu do NVDA, submenu Preferências, caixa de
diálogo Configurações.

Ele oferece as seguintes opções:

* Comprimento da linha do relatório: Você pode digitar ou escolher um
  comprimento de linha (número de caracteres entre 0 e 600), que será
  anunciado por um tom alto quando for atingido. (O valor padrão é 80
  caracteres).
* Número máximo de bipes para notificação de início de linha: Você pode
  digitar ou selecionar um valor entre 0 e 600. O valor padrão é 0.
* Número máximo de bipes para notificação de fim de linha: Você pode digitar
  ou selecionar um valor entre 0 e 600. O valor padrão é 0.
* Pitch do som para o início da linha: Você pode digitar ou selecionar um
  valor entre 20 e 20000. (O valor padrão é 400 hertzs).
* Comprimento do som para o início da linha: Você pode digitar ou selecionar
  um valor entre 20 e 2000. (O valor padrão é 50 milissegundos).
* Testar som para início da linha: Pressione esse botão para testar o som
  configurado para o início da linha.
* Pitch do som para o fim da linha: Você pode digitar ou selecionar um valor
  entre 20 e 20000. (O valor padrão é 1000 hertzs).
* Comprimento do som para o fim da linha: Você pode digitar ou selecionar um
  valor entre 20 e 2000. (O valor padrão é 50 milissegundos).
* Testar som para fim de linha: Pressione esse botão para testar o som
  configurado para o fim da linha.

## Comandos ##

Você pode modificar os gestos para os seguintes comandos por meio do menu do
NVDA, submenu Preferências, caixa de diálogo Gestos de entrada:

* NVDA+ctrl+shift+l: Quando possível, informa o comprimento da linha atual
  (categoria do cursor do sistema).
* Não atribuído: Mostra a caixa de diálogo de configurações do Cursor
  Locator (categoria Config).

## Alterações para a versão 3.0 ##



* Compatível com o NVDA 2023.1.



## Alterações para a versão 2.0 ##

* Foi adicionada a capacidade de repetir notificações ao chegar ao final e

  ao início da linha.
* Adicionado suporte para documentos do Office e Notepad no Windows 11.


## Alterações para a versão 1.0 ##

* Versão inicial

[[!tag dev stable]]
