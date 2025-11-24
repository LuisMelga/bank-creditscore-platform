module "eks_prod" {
  source       = "../../modules/eks"
  cluster_name = "creditscore"
  env          = "prod"
  region       = "us-east-1"
}
