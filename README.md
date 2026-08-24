# CHATÃO 💬

## Versão

### **v0.1.1**

## Sobre o projeto

O projeto tem como finalidade, construir um ambiente de conversa entre pessoas, algo semelhante ao Whatsapp, onde a pessoa deve se cadastrar na página de login para conseguir criar chats com quem quiser.

## Como me cadastrar?

1. O cadastro exige apenas:
    - Nome;
    - Telefone;
    - Email;
    - Data de nascimento.
    
> [!NOTE]
> Você também pode criar um nickname bem irado!

## Diagrama
~~~mermaid
classDiagram
    class Usuario {
        -string nome
        -string nickname
        -string email
        -string telefone
        -date data_nascimento
        +nome() string
        +nome(string nome) void
        +nickname() string
        +nickname(string nickname) void
        +email() string
        +email(string email) void
        +telefone() string
        +telefone(string telefone) void
        +data_nascimento() date
        +data_nascimento(date data_nascimento) void
    }
~~~