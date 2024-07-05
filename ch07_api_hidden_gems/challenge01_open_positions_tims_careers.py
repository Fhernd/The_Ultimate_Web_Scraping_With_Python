from dataclasses import dataclass
from typing import List

import requests


@dataclass
class JobPosition:
    id: str
    title: str
    work_mode: str
    distance: float
    requirements: str
    
    def __str__(self):
        return f'ID: {self.id}\nTitle: {self.title}\nWork Mode: {self.work_mode}\nDistance: {self.distance}\nRequirements: {self.requirements}\n'


def extract_job_positions(results, lat, lng, postal_code) -> List[JobPosition]:
    job_positions = []
    
    for i in range(1, results + 1):
        url = f'https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters[brand.id]=58bd9e7f472bd&filters[lat]={lat}&filters[lng]={lng}&filters[distance]=2290599.375&sort[distance]=asc'
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()['data']
        
        for job in data:
            id = job['id']
            
            attributes = job['attributes']
            title = attributes['title']
            work_mode = 'Full-time' if attributes['full_time'] else 'Part-time' if attributes['part_time'] else 'Undefined'
            distance = attributes['distance']
            requirements = ', '.join(attributes['requirements'])

            job_position = JobPosition(
                id=id,
                title=title,
                work_mode=work_mode,
                distance=distance,
                requirements=requirements
            )
            job_positions.append(job_position)
    
    return job_positions

def main():
    """
    Main function to extract job positions from Tim's Careers API.
    """
    MAX_RESULTS_PER_PAGE = 24
    lat = 29.784753
    lng = -95.361416
    postal_code = '77003'
    results = 10
    results = results // MAX_RESULTS_PER_PAGE + 1
    
    job_positions = extract_job_positions(results, lat, lng, postal_code)
    
    for job_position in job_positions:
        print(job_position)
        print()


if __name__ == '__main__':
    main()
