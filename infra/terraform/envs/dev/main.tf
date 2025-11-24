module "eks_dev" {
  source       = "../../modules/eks"
  cluster_name = "creditscore"
  env          = "dev"
  region       = "us-east-1"
}
