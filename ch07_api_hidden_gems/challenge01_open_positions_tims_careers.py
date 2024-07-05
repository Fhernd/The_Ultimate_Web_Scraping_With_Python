from dataclasses import dataclass


@dataclass
class JobPosition:
    title: str
    work_mode: str
    distance: float
    requirements: str


def extract_job_positions(url, results, lat, lng, postal_code):
    pass

def main():
    """
    Main function to extract job positions from Tim's Careers API.
    """
    lat = 29.784753
    lng = -95.361416
    postal_code = '77003'
    results = 10
    
    url = f'https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd&filters[lat]={lat}&filters[lng]={lng}&filters[distance]=2290599.375&sort[distance]=asc'
    
    extract_job_positions(url, results, lat, lng, postal_code)


if __name__ == '__main__':
    main()
