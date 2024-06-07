from pydantic import Field
from prefect.workers.base import BaseJobConfiguration, BaseWorker, BaseWorkerResult

class NomadWorkerConfiguration(BaseJobConfiguration):
    memory: str = Field(
        default="2048Mi",
        description="Memory allocation for the execution job. Default: 2GB RAM.",
        # TODO: Check what the nomad job API looks like
        template="{{ memory_request }}Mi"
    )
    cpu: str = Field(
        default="500m",
        description="CPU allocation for the execution job. Default: 0.5 CPU.",
        # TODO: Check what the nomad job API looks like
        template="{{ cpu_request }}m"
    )
    
    
