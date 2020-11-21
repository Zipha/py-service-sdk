ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week
SECRET_KEY = "a77ec4c45a3bf81f68882a5f2398c26e953d16dc5c3c63c34730f23b19654e31"
SECRET_SALT = b'CfN0hksM0ynTsSmgUiJo-ZnwkHnYKHFpsIoY_1gQY_k='
EMAIL_VERIFY_TOKEN_EXPIRE_MINUTES = 60 * 24
RESET_PASSWORD_TOKEN_EXPIRE_MINUTES = 10


# Platfor Account Types
candidate_account_type = 'Candidate'
institution_account_type = 'Institution'
expert_account_type = 'Expert'
mentor_account_type = 'Mentor'


# Kafka Topic List
human_profile_create_topic = "human_profile_create"
human_profile_featch_topic = "profile_featch"
human_profile_result_topic = "human_profile_result"
institution_profile_create_topic = "institution_profile_create"
institution_profile_get_topic = "institution_profile_get"
institution_profile_get_result_topic = "institution_profile_get_result"
job_role_create_topic  ="job_role_create"
job_role_create_result_topic  ="job_role_create_result"
job_role_search_keyword_topic ="job_role_search_keyword"
job_role_search_keyword_result_topic ="job_role_search_keyword_result"
job_role_search_result_topic = "job_role_search_result"
job_role_search_topic = "job_role_search"
jobs_search_topic = "jobs_search"
jobs_search_results_topic = "jobs_search_results"
service_object_create_topic = "service_object_create"
service_object_update_topic = "service_object_update"
candidate_applied_jobs_get_topic ="candidate_applied_jobs_get"
candidate_applied_jobs_result_topic = "candidate_applied_jobs_result"
profile_update_topic = "human_profile_update"
suggested_job_update_topic = "suggested_job_update"
applied_job_update_topic  = "applied_job_update"
job_expiry_update_topic   = "job_expiry_update"
job_group  = "job"
profile_group = "profile"
