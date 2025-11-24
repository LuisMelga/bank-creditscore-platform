name: Deploy PROD

on:
  push:
    branches: ["main"]

jobs:
  approval:
    runs-on: ubuntu-latest
    steps:
      - name: Esperar aprobación manual
        uses: trstringer/manual-approval@v1
        with:
          approvers: lmelgarejo, seguridad, plataforma
          minimum-approvals: 2
          timeout-minutes: 1440

  deploy-prod:
    needs: approval
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: AWS Auth (PROD)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-prod-role
          aws-region: us-east-1

      - name: Update kubeconfig PROD
        run: |
          aws eks update-kubeconfig --name creditscore-prod --region us-east-1

      - name: Apply K8s manifests PROD
        run: |
          kubectl apply -f infra/k8s/prod/
