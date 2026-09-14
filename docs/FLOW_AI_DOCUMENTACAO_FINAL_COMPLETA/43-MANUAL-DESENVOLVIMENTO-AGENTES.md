# FLOW AI — MANUAL DE DESENVOLVIMENTO PARA AGENTES DE IA

## REGRA ZERO
Antes de modificar o projeto, o agente deve entender a arquitetura existente e procurar implementação equivalente.

## 1. Não duplicar
Nunca criar uma tela, endpoint, service, tabela ou integração sem procurar primeiro.

## 2. Visual
Seguir o Design System FLOW:
- tema claro;
- fundo `#F8F9FF`;
- cards brancos;
- primary `#6D28FF`;
- secondary `#4DA3FF`;
- accent `#FF2E9E`;
- dark textual `#11124B`;
- bordas suaves;
- cantos arredondados;
- sombras discretas.

## 3. Backend
Respeitar:
```text
API
→ Serializer
→ Service
→ Repository/ORM
→ Database
```

## 4. Integrações
Usar adapter. Nunca chamar API externa diretamente de componente frontend ou domínio.

## 5. IA
Tools precisam de schema, permissão, risco e executor.

## 6. Banco
Alterações exigem migration.

## 7. API
Alterações incompatíveis exigem versionamento.

## 8. Segurança
Nunca:
- imprimir secret;
- commitar `.env`;
- colocar API key no frontend;
- ignorar autorização;
- confiar no cliente para permissão.

## 9. Testes
Toda alteração relevante deve adicionar/ajustar testes.

## 10. Estados
Tela deve considerar loading, vazio, erro e sucesso.

## 11. Processo obrigatório
```text
LER
→ PESQUISAR
→ PLANEJAR
→ IMPLEMENTAR
→ TESTAR
→ REVISAR
→ DOCUMENTAR
```

## 12. Antes do commit
Verificar:
- lint;
- testes;
- TypeScript/Python;
- migrations;
- segurança;
- duplicidade;
- documentação.

## 13. Proibição
Não alterar arquitetura estrutural por conveniência sem registrar decisão técnica.

## 14. Regra de conclusão
“Funcionou localmente” não é suficiente. A tarefa só é concluída quando contrato, testes, estados, segurança e documentação estiverem coerentes.
