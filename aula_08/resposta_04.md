## Discuta como é feita as assinaturas na plataforma `SOUGOV.BR`. Onde são armazenadas as chaves privadas?

No modelo usado pelo SouGov.br:

- O usuário não possui a chave privada localmente (exceto se estiver usando um certificado digital ICP-Brasil).

- A chave privada é armazenada e gerenciada em nuvem por um HSM (Hardware Security Module) controlado pelo governo.

- A plataforma atua como um serviço de assinatura centralizado, onde a chave privada do usuário é protegida e operada por servidores confiáveis, sem ser exposta diretamente ao usuário ou à aplicação cliente.

- Quando o usuário autoriza uma assinatura, a plataforma realiza a operação criptográfica dentro do HSM ou sistema seguro.

-  Esse modelo garante segurança, integridade e não repúdio, ao mesmo tempo em que simplifica o uso para usuários que não têm certificado ICP-Brasil instalado.
