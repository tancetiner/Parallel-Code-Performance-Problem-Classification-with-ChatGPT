from GptApi import GptApi
import json

gpt = GptApi()
gpt.start_conversation()
"""
"You are a parallel computing expert. I will provide you a source code in C or C++ and I want you to classify if there is an inefficiency problem in the code. If there is an problem, I want you to classify this problem from the following list: ["Memory/Data locality",
    "Micro-architectural inefficiency",
    "Vector/SIMD parallelism",
    "GPU parallelism",
    "Instruction level parallelism",
    "Task parallelism",
    "small parallel region",
    "Inefficeint thread mapping / inefficient block size / Load imbalance",
    "Under-parallelization",
    "Over-Parallelization",
    "Unncessary locks",
    "Unncessary strong memory consistency",
    "Lock management overhead",
    "Unnecessary synchronization",
    "Unnecessary process communiction",
    "Unnecessary operation/traversal/function call",
    "Redundant operation",
    "Expensive operation",
    "Frequent  function call",
    "Inefficient data-structure library",
    "Usage of improper data type",
    "memory leak",
    "repreated memory allocation",
    "Redundant memory allocation",
    "Slower memory allocation library call",
    "Insufficient memory",
    "unnecessary data copy",
    "sequential I/O operation",
    "over parallelization",
    "boundary condition check",
    "Unintentional Programming logic error",
    "Inefficiency due to new compiler version "
  ] and return an answer with the following format: Type: classified_type. I may provide the source code within multiple prompts so in order to indicate the source code to finish I'll put '--END--' at the end of the code."

"""
