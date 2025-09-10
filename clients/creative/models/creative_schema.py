from typing import List

from pydantic import BaseModel, Field

class CreativeMapSchema(BaseModel):
    """
    Схема карты креативов.
    """
    communication_channel: str = Field(default="user_object_over_map", description="Канал коммуникации")
    creative_map_name: str = Field(default="создал", description="Название карты креативов")
    campaign_id: int = Field(default=51313, description="Идентификатор кампании")
    creative_request_id: int = Field(default=79625, description="Идентификатор запроса креатива")
    creative_map_id: str = Field(default="e37a4c40-f4c7-49fe-857c-21a8c230c6e7", description="Идентификатор карты креативов")
    target_app: str = Field(default="go", description="Целевое приложение")
    is_used_in_action: bool = Field(default=False, description="Используется ли в действии")
    is_used_in_single_verification: bool = Field(default=False, description="Используется ли в единичной верификации")

class GetCreativeMapListResponseSchema(BaseModel):
    """
    Схема ответа со списком карт креативов.
    """
    __root__: List[CreativeMapSchema] = Field(default_factory=lambda: [CreativeMapSchema()], description="Список карт креативов")


class CreativeMapIdWithVersionSchema(BaseModel):
    """
    Схема идентификатора карты креативов с версией.
    """
    id: str = Field(default="79517ce5-d2af-4666-a3e5-8eaf3c99053d", description="Уникальный идентификатор карты креативов")
    version: int = Field(default=2, description="Версия карты креативов")


class DeeplinkSchema(BaseModel):
    """
    Схема диплинка для перехода в приложение.
    """
    obj_type: str = Field(default="deeplink_v1", description="Тип объекта диплинка")
    url: str = Field(default="yandextaxi://promocode", description="URL диплинка для перехода")


class MediaSchema(BaseModel):
    """
    Схема медиа контента креатива.
    """
    type: str = Field(default="image_tag", description="Тип медиа контента")
    image_tag: str = Field(default="achievements__refferal_for_sharing_wo_yandex", description="Тег изображения для отображения")


class DataSchema(BaseModel):
    """
    Схема данных креатива.
    """
    dynamic_type: str = Field(default="object_over_map", description="Тип динамического контента")
    marketing_text: str = Field(default="123", description="Маркетинговый текст")
    media: MediaSchema = Field(default_factory=MediaSchema, description="Медиа контент")


class LocaleWithContentSchema(BaseModel):
    """
    Схема локализованного контента креатива.
    """
    locale_language: str = Field(default="ru-Русский", description="Язык локали")
    deeplink: DeeplinkSchema = Field(default_factory=DeeplinkSchema, description="Диплинк для данной локали")
    data: DataSchema = Field(default_factory=DataSchema, description="Данные контента для локали")


class CreateCreativeCmsRequestSchema(BaseModel):
    """
    Схема запроса на создание креатива в CMS.
    """
    communication_channel: str = Field(default="object_over_map", description="Канал коммуникации")
    creative_map_id_with_version: CreativeMapIdWithVersionSchema = Field(default_factory=CreativeMapIdWithVersionSchema, description="Идентификатор и версия карты креативов")
    locales_with_content: List[LocaleWithContentSchema] = Field(default_factory=lambda: [LocaleWithContentSchema()], description="Список локалей с контентом")


class CreativeIdWithVersion(BaseModel):
    """
    Схема идентификатора креатива с версией.
    """
    id: str  # Уникальный идентификатор креатива
    version: int  # Версия креатива


class CreativeMapIdWithVersion(BaseModel):
    """
    Схема идентификатора карты креативов с версией.
    """
    id: str  # Уникальный идентификатор карты креативов
    version: int  # Версия карты креативов


class CreateCreativeCmsResponseSchema(BaseModel):
    """
    Схема ответа на создание креатива в CMS.
    """
    creative_id_with_version: CreativeIdWithVersion  # Идентификатор и версия созданного креатива
    creative_map_id_with_version: CreativeMapIdWithVersion  # Идентификатор и версия карты креативов


class CreateCreativeMapRequestSchema(BaseModel):
    """
    Схема запроса на создание карты креативов.
    """
    creative_map_name: str = Field(default="test_creative_map", description="Название карты креативов")
    communication_channel: str = Field(default="user_object_over_map", description="Канал коммуникации")
    target_app: str = Field(default="go", description="Целевое приложение")


class CreateCreativeMapResponseSchema(BaseModel):
    """
    Схема ответа на создание карты креативов.
    """
    creative_map_id: str  # Уникальный идентификатор созданной карты креативов
