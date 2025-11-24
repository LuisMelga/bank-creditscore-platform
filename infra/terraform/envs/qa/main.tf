module "eks_qa" {
  source       = "../../modules/eks"
  cluster_name = "creditscore"
  env          = "qa"
  region       = "us-east-1"
}
