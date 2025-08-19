# API

Types:

```python
from arbi.types import Chunk, ChunkMetadata
```

Methods:

- <code title="get /api">client.api.<a href="./src/arbi/resources/api/api.py">index</a>() -> object</code>

## User

Types:

```python
from arbi.types.api import Token, User, UserListWorkspacesResponse, UserLogoutResponse
```

Methods:

- <code title="get /api/user/workspaces">client.api.user.<a href="./src/arbi/resources/api/user/user.py">list_workspaces</a>() -> <a href="./src/arbi/types/api/user_list_workspaces_response.py">UserListWorkspacesResponse</a></code>
- <code title="post /api/user/login">client.api.user.<a href="./src/arbi/resources/api/user/user.py">login</a>(\*\*<a href="src/arbi/types/api/user_login_params.py">params</a>) -> <a href="./src/arbi/types/api/token.py">Token</a></code>
- <code title="post /api/user/logout">client.api.user.<a href="./src/arbi/resources/api/user/user.py">logout</a>() -> <a href="./src/arbi/types/api/user_logout_response.py">UserLogoutResponse</a></code>
- <code title="post /api/user/token_refresh">client.api.user.<a href="./src/arbi/resources/api/user/user.py">refresh_token</a>() -> <a href="./src/arbi/types/api/token.py">Token</a></code>
- <code title="post /api/user/register">client.api.user.<a href="./src/arbi/resources/api/user/user.py">register</a>(\*\*<a href="src/arbi/types/api/user_register_params.py">params</a>) -> <a href="./src/arbi/types/api/user/user.py">User</a></code>
- <code title="get /api/user/me">client.api.user.<a href="./src/arbi/resources/api/user/user.py">retrieve_current</a>() -> <a href="./src/arbi/types/api/user/user.py">User</a></code>

### Settings

Types:

```python
from arbi.types.api.user import SettingRetrieveResponse
```

Methods:

- <code title="get /api/user/settings">client.api.user.settings.<a href="./src/arbi/resources/api/user/settings.py">retrieve</a>() -> <a href="./src/arbi/types/api/user/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="patch /api/user/settings">client.api.user.settings.<a href="./src/arbi/resources/api/user/settings.py">update</a>(\*\*<a href="src/arbi/types/api/user/setting_update_params.py">params</a>) -> None</code>

## SSO

Types:

```python
from arbi.types.api import SSOInviteResponse, SSOLoginResponse, SSORotatePasscodeResponse
```

Methods:

- <code title="post /api/sso/invite">client.api.sso.<a href="./src/arbi/resources/api/sso.py">invite</a>(\*\*<a href="src/arbi/types/api/sso_invite_params.py">params</a>) -> <a href="./src/arbi/types/api/sso_invite_response.py">SSOInviteResponse</a></code>
- <code title="post /api/sso/login">client.api.sso.<a href="./src/arbi/resources/api/sso.py">login</a>(\*\*<a href="src/arbi/types/api/sso_login_params.py">params</a>) -> <a href="./src/arbi/types/api/sso_login_response.py">SSOLoginResponse</a></code>
- <code title="post /api/sso/rotate_passcode">client.api.sso.<a href="./src/arbi/resources/api/sso.py">rotate_passcode</a>() -> <a href="./src/arbi/types/api/sso_rotate_passcode_response.py">SSORotatePasscodeResponse</a></code>

## Workspace

Types:

```python
from arbi.types.api import (
    Workspace,
    WorkspaceDeleteResponse,
    WorkspaceListConversationsResponse,
    WorkspaceListDoctagsResponse,
    WorkspaceListDocumentsResponse,
    WorkspaceListTagsResponse,
    WorkspaceListUsersResponse,
    WorkspaceRemoveUserResponse,
    WorkspaceRetrieveStatsResponse,
    WorkspaceShareResponse,
)
```

Methods:

- <code title="patch /api/workspace/{workspace_ext_id}">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">update</a>(workspace_ext_id, \*\*<a href="src/arbi/types/api/workspace_update_params.py">params</a>) -> <a href="./src/arbi/types/api/workspace.py">Workspace</a></code>
- <code title="delete /api/workspace/{workspace_ext_id}">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">delete</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_delete_response.py">WorkspaceDeleteResponse</a></code>
- <code title="post /api/workspace/create_protected">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">create_protected</a>(\*\*<a href="src/arbi/types/api/workspace_create_protected_params.py">params</a>) -> <a href="./src/arbi/types/api/workspace.py">Workspace</a></code>
- <code title="get /api/workspace/{workspace_ext_id}/conversations">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">list_conversations</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_list_conversations_response.py">WorkspaceListConversationsResponse</a></code>
- <code title="get /api/workspace/{workspace_ext_id}/doctags">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">list_doctags</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_list_doctags_response.py">WorkspaceListDoctagsResponse</a></code>
- <code title="get /api/workspace/{workspace_ext_id}/documents">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">list_documents</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_list_documents_response.py">WorkspaceListDocumentsResponse</a></code>
- <code title="get /api/workspace/{workspace_ext_id}/tags">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">list_tags</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_list_tags_response.py">WorkspaceListTagsResponse</a></code>
- <code title="get /api/workspace/{workspace_ext_id}/users">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">list_users</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_list_users_response.py">WorkspaceListUsersResponse</a></code>
- <code title="delete /api/workspace/{workspace_ext_id}/user">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">remove_user</a>(workspace_ext_id, \*\*<a href="src/arbi/types/api/workspace_remove_user_params.py">params</a>) -> <a href="./src/arbi/types/api/workspace_remove_user_response.py">WorkspaceRemoveUserResponse</a></code>
- <code title="get /api/workspace/{workspace_ext_id}/stats">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">retrieve_stats</a>(workspace_ext_id) -> <a href="./src/arbi/types/api/workspace_retrieve_stats_response.py">WorkspaceRetrieveStatsResponse</a></code>
- <code title="post /api/workspace/{workspace_ext_id}/share">client.api.workspace.<a href="./src/arbi/resources/api/workspace.py">share</a>(workspace_ext_id, \*\*<a href="src/arbi/types/api/workspace_share_params.py">params</a>) -> <a href="./src/arbi/types/api/workspace_share_response.py">WorkspaceShareResponse</a></code>

## Document

Types:

```python
from arbi.types.api import (
    Doc,
    DocumentUpdateResponse,
    DocumentDeleteResponse,
    DocumentRetrieveParsedStageResponse,
    DocumentRetrieveTagsResponse,
)
```

Methods:

- <code title="get /api/document/{document_ext_id}">client.api.document.<a href="./src/arbi/resources/api/document/document.py">retrieve</a>(document_ext_id) -> <a href="./src/arbi/types/api/doc.py">Doc</a></code>
- <code title="patch /api/document/{document_ext_id}">client.api.document.<a href="./src/arbi/resources/api/document/document.py">update</a>(document_ext_id, \*\*<a href="src/arbi/types/api/document_update_params.py">params</a>) -> <a href="./src/arbi/types/api/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="delete /api/document/{document_ext_id}">client.api.document.<a href="./src/arbi/resources/api/document/document.py">delete</a>(document_ext_id) -> <a href="./src/arbi/types/api/document_delete_response.py">DocumentDeleteResponse</a></code>
- <code title="get /api/document/{document_ext_id}/download">client.api.document.<a href="./src/arbi/resources/api/document/document.py">retrieve_download</a>(document_ext_id) -> object</code>
- <code title="get /api/document/{document_ext_id}/parsed-{stage}">client.api.document.<a href="./src/arbi/resources/api/document/document.py">retrieve_parsed_stage</a>(stage, \*, document_ext_id) -> <a href="./src/arbi/types/api/document_retrieve_parsed_stage_response.py">DocumentRetrieveParsedStageResponse</a></code>
- <code title="get /api/document/{doc_ext_id}/tags">client.api.document.<a href="./src/arbi/resources/api/document/document.py">retrieve_tags</a>(doc_ext_id) -> <a href="./src/arbi/types/api/document_retrieve_tags_response.py">DocumentRetrieveTagsResponse</a></code>
- <code title="get /api/document/{document_ext_id}/view">client.api.document.<a href="./src/arbi/resources/api/document/document.py">retrieve_view</a>(document_ext_id, \*\*<a href="src/arbi/types/api/document_retrieve_view_params.py">params</a>) -> object</code>
- <code title="post /api/document/upload">client.api.document.<a href="./src/arbi/resources/api/document/document.py">upload</a>(\*\*<a href="src/arbi/types/api/document_upload_params.py">params</a>) -> object</code>

### Annotation

Types:

```python
from arbi.types.api.document import DocTag, AnnotationDeleteResponse
```

Methods:

- <code title="post /api/document/{doc_ext_id}/annotation">client.api.document.annotation.<a href="./src/arbi/resources/api/document/annotation.py">create</a>(doc_ext_id, \*\*<a href="src/arbi/types/api/document/annotation_create_params.py">params</a>) -> <a href="./src/arbi/types/api/document/doc_tag.py">DocTag</a></code>
- <code title="patch /api/document/{doc_ext_id}/annotation/{doctag_ext_id}">client.api.document.annotation.<a href="./src/arbi/resources/api/document/annotation.py">update</a>(doctag_ext_id, \*, doc_ext_id, \*\*<a href="src/arbi/types/api/document/annotation_update_params.py">params</a>) -> <a href="./src/arbi/types/api/document/doc_tag.py">DocTag</a></code>
- <code title="delete /api/document/{doc_ext_id}/annotation/{doctag_ext_id}">client.api.document.annotation.<a href="./src/arbi/resources/api/document/annotation.py">delete</a>(doctag_ext_id, \*, doc_ext_id) -> <a href="./src/arbi/types/api/document/annotation_delete_response.py">AnnotationDeleteResponse</a></code>

## Conversation

Types:

```python
from arbi.types.api import (
    ConversationDeleteResponse,
    ConversationDeleteMessageResponse,
    ConversationRetrieveThreadsResponse,
    ConversationShareResponse,
    ConversationUpdateTitleResponse,
)
```

Methods:

- <code title="delete /api/conversation/{conversation_ext_id}">client.api.conversation.<a href="./src/arbi/resources/api/conversation/conversation.py">delete</a>(conversation_ext_id) -> <a href="./src/arbi/types/api/conversation_delete_response.py">ConversationDeleteResponse</a></code>
- <code title="delete /api/conversation/message/{message_ext_id}">client.api.conversation.<a href="./src/arbi/resources/api/conversation/conversation.py">delete_message</a>(message_ext_id) -> <a href="./src/arbi/types/api/conversation_delete_message_response.py">ConversationDeleteMessageResponse</a></code>
- <code title="get /api/conversation/{conversation_ext_id}/threads">client.api.conversation.<a href="./src/arbi/resources/api/conversation/conversation.py">retrieve_threads</a>(conversation_ext_id) -> <a href="./src/arbi/types/api/conversation_retrieve_threads_response.py">ConversationRetrieveThreadsResponse</a></code>
- <code title="post /api/conversation/{conversation_ext_id}/share">client.api.conversation.<a href="./src/arbi/resources/api/conversation/conversation.py">share</a>(conversation_ext_id) -> <a href="./src/arbi/types/api/conversation_share_response.py">ConversationShareResponse</a></code>
- <code title="patch /api/conversation/{conversation_ext_id}/title">client.api.conversation.<a href="./src/arbi/resources/api/conversation/conversation.py">update_title</a>(conversation_ext_id, \*\*<a href="src/arbi/types/api/conversation_update_title_params.py">params</a>) -> <a href="./src/arbi/types/api/conversation_update_title_response.py">ConversationUpdateTitleResponse</a></code>

### User

Types:

```python
from arbi.types.api.conversation import UserCreateResponse, UserDeleteAllResponse
```

Methods:

- <code title="post /api/conversation/{conversation_ext_id}/user">client.api.conversation.user.<a href="./src/arbi/resources/api/conversation/user.py">create</a>(conversation_ext_id, \*\*<a href="src/arbi/types/api/conversation/user_create_params.py">params</a>) -> <a href="./src/arbi/types/api/conversation/user_create_response.py">UserCreateResponse</a></code>
- <code title="delete /api/conversation/{conversation_ext_id}/user">client.api.conversation.user.<a href="./src/arbi/resources/api/conversation/user.py">delete_all</a>(conversation_ext_id, \*\*<a href="src/arbi/types/api/conversation/user_delete_all_params.py">params</a>) -> <a href="./src/arbi/types/api/conversation/user_delete_all_response.py">UserDeleteAllResponse</a></code>

## Assistant

Types:

```python
from arbi.types.api import MessageInput
```

Methods:

- <code title="post /api/assistant/retrieve">client.api.assistant.<a href="./src/arbi/resources/api/assistant.py">retrieve</a>(\*\*<a href="src/arbi/types/api/assistant_retrieve_params.py">params</a>) -> object</code>
- <code title="post /api/assistant/query">client.api.assistant.<a href="./src/arbi/resources/api/assistant.py">query</a>(\*\*<a href="src/arbi/types/api/assistant_query_params.py">params</a>) -> object</code>

## Health

Types:

```python
from arbi.types.api import (
    HealthRetrieveAppResponse,
    HealthRetrieveModelsResponse,
    HealthRetrieveRemoteModelsResponse,
    HealthRetrieveServicesResponse,
)
```

Methods:

- <code title="get /api/health/app">client.api.health.<a href="./src/arbi/resources/api/health.py">retrieve_app</a>() -> <a href="./src/arbi/types/api/health_retrieve_app_response.py">HealthRetrieveAppResponse</a></code>
- <code title="get /api/health/models">client.api.health.<a href="./src/arbi/resources/api/health.py">retrieve_models</a>() -> <a href="./src/arbi/types/api/health_retrieve_models_response.py">HealthRetrieveModelsResponse</a></code>
- <code title="get /api/health/remote-models">client.api.health.<a href="./src/arbi/resources/api/health.py">retrieve_remote_models</a>() -> <a href="./src/arbi/types/api/health_retrieve_remote_models_response.py">HealthRetrieveRemoteModelsResponse</a></code>
- <code title="get /api/health/services">client.api.health.<a href="./src/arbi/resources/api/health.py">retrieve_services</a>() -> <a href="./src/arbi/types/api/health_retrieve_services_response.py">HealthRetrieveServicesResponse</a></code>

## Tag

Types:

```python
from arbi.types.api import (
    TagOperation,
    TagCreateResponse,
    TagUpdateResponse,
    TagApplyResponse,
    TagDeleteDeleteResponse,
    TagDeleteRemoveResponse,
    TagRetrieveDocsResponse,
)
```

Methods:

- <code title="post /api/tag/create">client.api.tag.<a href="./src/arbi/resources/api/tag.py">create</a>(\*\*<a href="src/arbi/types/api/tag_create_params.py">params</a>) -> <a href="./src/arbi/types/api/tag_create_response.py">TagCreateResponse</a></code>
- <code title="patch /api/tag/{tag_ext_id}">client.api.tag.<a href="./src/arbi/resources/api/tag.py">update</a>(tag_ext_id, \*\*<a href="src/arbi/types/api/tag_update_params.py">params</a>) -> <a href="./src/arbi/types/api/tag_update_response.py">TagUpdateResponse</a></code>
- <code title="post /api/tag/{tag_ext_id}/apply">client.api.tag.<a href="./src/arbi/resources/api/tag.py">apply</a>(tag_ext_id, \*\*<a href="src/arbi/types/api/tag_apply_params.py">params</a>) -> <a href="./src/arbi/types/api/tag_apply_response.py">TagApplyResponse</a></code>
- <code title="delete /api/tag/{tag_ext_id}/delete">client.api.tag.<a href="./src/arbi/resources/api/tag.py">delete_delete</a>(tag_ext_id) -> <a href="./src/arbi/types/api/tag_delete_delete_response.py">TagDeleteDeleteResponse</a></code>
- <code title="delete /api/tag/{tag_ext_id}/remove">client.api.tag.<a href="./src/arbi/resources/api/tag.py">delete_remove</a>(tag_ext_id, \*\*<a href="src/arbi/types/api/tag_delete_remove_params.py">params</a>) -> <a href="./src/arbi/types/api/tag_delete_remove_response.py">TagDeleteRemoveResponse</a></code>
- <code title="get /api/tag/{tag_ext_id}/docs">client.api.tag.<a href="./src/arbi/resources/api/tag.py">retrieve_docs</a>(tag_ext_id) -> <a href="./src/arbi/types/api/tag_retrieve_docs_response.py">TagRetrieveDocsResponse</a></code>

## Configs

Types:

```python
from arbi.types.api import (
    ChunkerConfig,
    DocumentDateExtractorLlmConfig,
    EmbedderConfig,
    ModelCitationConfig,
    ParserConfig,
    QueryLlmConfig,
    RerankerConfig,
    RetrieverConfig,
    TitleLlmConfig,
    ConfigUpdateResponse,
    ConfigRetrieveVersionsResponse,
)
```

Methods:

- <code title="post /api/configs/">client.api.configs.<a href="./src/arbi/resources/api/configs.py">update</a>(\*\*<a href="src/arbi/types/api/config_update_params.py">params</a>) -> <a href="./src/arbi/types/api/config_update_response.py">ConfigUpdateResponse</a></code>
- <code title="get /api/configs/schema">client.api.configs.<a href="./src/arbi/resources/api/configs.py">retrieve_schema</a>() -> object</code>
- <code title="get /api/configs/versions">client.api.configs.<a href="./src/arbi/resources/api/configs.py">retrieve_versions</a>() -> <a href="./src/arbi/types/api/config_retrieve_versions_response.py">ConfigRetrieveVersionsResponse</a></code>
