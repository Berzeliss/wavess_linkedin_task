import os
import pandas as pd

def audience_ranking(member: dict, icp_roles: list, icp_companies: list) -> float:
    """Calculating an audience ranking score based on member's profile and ICP criteria.
    
    Parameters:
    member (dict): A dictionary containing member's profile information.
    icp_roles (list): A list of ideal customer profile roles.
    icp_companies (list): A list of ideal customer profile companies.
    
    Returns:
    float: A score representing how well the member matches the ICP criteria."""    
    
    score = 0.0
    
    # Role Match - If the member's job title matches any of the ICP roles, add to score
    if member["job_title"].lower() in [r.lower() for r in icp_roles]:
        score += 2
        
    # Seniority boost
    if member["seniority"].lower() in ["mid", "senior"]:
        score += 1
        
    # Company Match - If the member's company matches any of the ICP companies, add to score
    if any(target.lower() in member["company"].lower() for target in icp_companies):
        score += 1
    
    # Keyword boost for relevant tech roles    
    keywords = ["ai", "data", "ml", "analytics"]
    if any(k in member["job_title"].lower() for k in keywords):
        score += 0.5
        
    return score
  
def determine_seniority(title: str) -> str:
    """Determining seniority level based on job title."""
    
    title_lower = title.lower()
    if any(x in title_lower for x in ["manager", "director", "lead", "chief", "vp", "head"]):
        return "senior"
    elif any(x in title_lower for x in ["intern", "student", "assistant", "associate"]):
        return "junior"
    else:
        return "mid"
    
def determine_company_type(company_name: str) -> str:
    """Infer company type from company name."""
    
    name_lower = company_name.lower()
    if any(x in name_lower for x in ["bank", "finance", "payment"]):
        return "Finance"
    elif any(x in name_lower for x in ["tech", "software", "ai", "data", "solution"]):
        return "Tech"
    elif any(x in name_lower for x in ["foundation", "initiative", "milkywire", "norrsken"]):
        return "Nonprofit"
    elif any(x in name_lower for x in ["agency", "marketing", "media"]):
        return "Agency"
    else:
        return "Other"

def main():
    
    # Defining the ICP criteria
    icp_roles = ["Data Scientist", "Product Manager", "AI Engineer"]
    icp_companies = ["Klarna", "DCsolution", "Solidgate", "WebBank", "Exponential Roadmap Initiative", "Milkywire", "Norrsken Foundation", "Medicidiom"]
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audience_csv = os.path.join(script_dir, "../data/raw/audience_samples.csv")
    output_csv = os.path.join(script_dir, "../outputs/audience_ranked.csv")
    
    df = pd.read_csv(audience_csv)
    
    df["seniority"] = df["job_title"].apply(determine_seniority)
    df["company_type"] = df["company"].apply(determine_company_type)
    
    
    
    #Calculate ICP relevance score for each audience member
    df["icp_score"] = df.apply(lambda row: audience_ranking(row, icp_roles, icp_companies), axis=1)
    df_sorted = df.sort_values(by="icp_score", ascending=False)
    
    df_sorted.to_csv(output_csv, index=False)
    
    print("Audience ranking done. Output saved to outputs/audience_ranked.csv")

if __name__ == "__main__":
    main()