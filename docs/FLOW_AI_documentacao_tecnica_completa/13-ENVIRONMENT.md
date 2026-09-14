# FLOW AI — ENVIRONMENT VARIABLES

## Regra
Este documento define nomes de configuração. Não inserir valores reais.

## Django
```env
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
DJANGO_ALLOWED_HOSTS=
DJANGO_CSRF_TRUSTED_ORIGINS=
```

## Database
```env
DATABASE_URL=
```

## Redis
```env
REDIS_URL=
```

## NVIDIA
```env
NVIDIA_API_KEY=
NVIDIA_BASE_URL=
NVIDIA_MODEL=
```

## Firebase
```env
FIREBASE_PROJECT_ID=
FIREBASE_CLIENT_EMAIL=
FIREBASE_PRIVATE_KEY=
```

## Meta
```env
META_APP_ID=
META_APP_SECRET=
META_REDIRECT_URI=
META_VERIFY_TOKEN=
```

## Cloudflare
```env
CLOUDFLARE_API_TOKEN=
CLOUDFLARE_ACCOUNT_ID=
```

## Frontend
```env
PUBLIC_API_BASE_URL=https://api-flow-ai.flowsocial.fun
PUBLIC_APP_URL=https://flow-ai.flowsocial.fun
```

## Regras
- `.env` não vai para Git;
- `.env.example` contém somente nomes;
- secrets diferentes por ambiente;
- rotação documentada;
- menor privilégio.
