#### What's Improved
- This version is now certified. 
- Added a new parameter `Exclude Observables` in `Submit Observables` action.
- Data Ingestion Changes: 
	- Changed the global variable name from `ThreatStreamLastIncidentPullTime` to dynamically created in format "AnomaliThreatStreamLastPullTime_{playbook_iri}"
	- Removed Data Ingestion Playbook `>> Anomali ThreatStream > Handle Macros`.
- Updated output schemas for following actions:
  - Approve IOC By Import ID
  - Reject IOC By Import ID
  - Get Sandbox Status of Submitted URL/File
#### What's Fixed
- Fixed an issue in which enrichment playbooks were encountering failures for indicators that were not found in the Anomali Threatstream Setup.
- Fixed a bug where Data Ingestion configuration failed with error "The 'modified_ts_gte' field does not allow filtering".
