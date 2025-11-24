module "eks_uat" {
  source       = "../../modules/eks"
  cluster_name = "creditscore"
  env          = "uat"
  region       = "us-east-1"
}
