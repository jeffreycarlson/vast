# VAST

This repro contains tools and reference materials to help build, analyze and debug VAST creative successfully on mobile devices.

## What Is VAST?

VAST is a Video Ad Serving Template for structuring ad tags that serve ads to video players. 

Version 4.0 is the latest version from the IAB. 

For more information about the VAST, visit the IAB's site:

* [VAST 4.0](http://www.iab.com/guidelines/digital-video-ad-serving-template-vast-4-0/)
* [VAST 3.0](http://www.iab.com/guidelines/digital-video-ad-serving-template-vast-3-0/)
* [VAST 2.0](http://www.iab.com/guidelines/digital-video-ad-serving-template-vast-2-0/)

## VAST Tools

A list of tools to help construct and debug VAST creative, specificially for mobile.

## VAST Elements and Attributes

| Elements | Attributes |     |     |     |     | 
| ---      | ---        | --- | --- | --- | --- |
| VAST |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | version | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Error |  | - | 3.0 | 4.0 | 4.1 | 
| VAST/Ad |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | sequence | - | 3.0 | 4.0 | 4.1 | 
|  | conditionalAd | - | - | 4.0 | 4.1 | 
|  | adType | - | - | - | 4.1 | 
| VAST/Ad/InLine |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/AdSystem |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | version | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/AdTitle |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Impression |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/AdServingId |  | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Category |  | - | - | 4.0 | 4.1 | 
|  | authority | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Description |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Advertiser |  | - | 3.0 | 4.0 | 4.1 | 
|  | id | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Pricing |  | - | 3.0 | 4.0 | 4.1 | 
|  | model | - | 3.0 | 4.0 | 4.1 | 
|  | currency | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Survey |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | type | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Error |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Expires |  | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;/ViewableImpression |  | - | - | 4.0 | 4.1 | 
|  | id | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Viewable |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NotViewable |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ViewUndetermined |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/AdVerifications |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Verification |  | - | - | 4.0 | 4.1 | 
|  | vendor | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/JavaScriptResource |  | - | - | 4.0 | 4.1 | 
|  | apiFramework | - | - | 4.0 | 4.1 | 
|  | browserOptional | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/FlashResource |  | - | - | 4.0 | 4.1 | 
|  | apiFramework | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ExecutableResource |  | - | - | - | 4.1 | 
|  | apiFramework | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  | - | - | - | 4.1 | 
|  | event | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ViewableImpression |  | - | - | 4.0 | - | 
|  | id | - | - | 4.0 | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/VerificationParameters |  | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Extensions |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Extension |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | type | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Creatives |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Creative |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | sequence | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | adId | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | apiFramework | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/UniversalAdId |  | - | - | 4.0 | 4.1 | 
|  | idRegistry | - | - | 4.0 | 4.1 | 
|  | idValue | - | - | 4.0 | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CreativeExtensions |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CreativeExtension |  | - | 3.0 | 4.0 | 4.1 | 
|  | type | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Linear |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | skipoffset | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Duration |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/AdParameters |  | - | 3.0 | 4.0 | 4.1 | 
|  | xmlEncoded | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/MediaFiles |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Mezzanine |  | - | - | 4.0 | 4.1 | 
|  | delivery | - | - | - | 4.1 | 
|  | type | - | - | - | 4.1 | 
|  | width | - | - | - | 4.1 | 
|  | height | - | - | - | 4.1 | 
|  | codec | - | - | - | 4.1 | 
|  | id | - | - | - | 4.1 | 
|  | fileSize | - | - | - | 4.1 | 
|  | mediaType | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/MediaFile |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | delivery | - | - | 4.0 | 4.1 | 
|  | type | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | bitrate | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | minBitrate | - | 3.0 | 4.0 | 4.1 | 
|  | maxBitrate | - | 3.0 | 4.0 | 4.1 | 
|  | width | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | height | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | scalable | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | maintainAspectRatio | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | codec | - | 3.0 | 4.0 | 4.1 | 
|  | apiFramework | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | fileSize | - | - | - | 4.1 | 
|  | mediaType | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/InteractiveCreativeFile |  | - | - | 4.0 | 4.1 | 
|  | apiFramework | - | - | 4.0 | 4.1 | 
|  | variableDuration | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ClosedCaptionFiles |  | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ClosedCaptionFile |  | - | - | - | 4.1 | 
|  | type | - | - | - | 4.1 | 
|  | language | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/VideoClicks |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ClickThrough |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ClickTracking |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CustomClick |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | event | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | offset | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Icons |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Icon |  | - | 3.0 | 4.0 | 4.1 | 
|  | program | - | 3.0 | 4.0 | 4.1 | 
|  | width | - | 3.0 | 4.0 | 4.1 | 
|  | height | - | 3.0 | 4.0 | 4.1 | 
|  | xPosition | - | 3.0 | 4.0 | 4.1 | 
|  | yPosition | - | 3.0 | 4.0 | 4.1 | 
|  | duration | - | 3.0 | 4.0 | 4.1 | 
|  | offset | - | 3.0 | 4.0 | 4.1 | 
|  | apiFramework | - | 3.0 | 4.0 | 4.1 | 
|  | pxratio | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/StaticResource |  | - | 3.0 | 4.0 | 4.1 | 
|  | creativeType | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IFrameResource |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/HTMLResource |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconClicks |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconClickThrough |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconClickTracking |  | - | 3.0 | 4.0 | 4.1 | 
|  | id | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconViewTracking |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinearAds |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinear |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id | 2.0 | 3.0 | - | - | 
|  | width | 2.0 | 3.0 | - | - | 
|  | height | 2.0 | 3.0 | - | - | 
|  | expandedWidth | 2.0 | 3.0 | - | - | 
|  | expandedHeight | 2.0 | 3.0 | - | - | 
|  | scalable | 2.0 | 3.0 | - | - | 
|  | maintainAspectRatio | 2.0 | 3.0 | - | - | 
|  | minSuggestedDuration | 2.0 | 3.0 | - | - | 
|  | apiFramework | 2.0 | 3.0 | - | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinearClickThrough |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinearClickTracking |  | - | 3.0 | 4.0 | 4.1 | 
|  | id | - | 3.0 | - | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | event | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/AdParameters |  | 2.0 | ?? | ?? | ?? | 
|  | xmlEncoded | - | ?? | ?? | ?? | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CompanionAds |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | required | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Companion |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | width | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | height | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | assetWidth | - | 3.0 | 4.0 | 4.1 | 
|  | assetHeight | - | 3.0 | 4.0 | 4.1 | 
|  | expandedWidth | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | expandedHeight | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | apiFramework | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | adSlotID | - | 3.0 | 4.0 | 4.1 | 
|  | pxratio | - | - | 4.0 | 4.1 | 
|  | renderingMode | - | - | - | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/StaticResource |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | creativeType | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IFrameResource |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/HTMLResource |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/AdParameters |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | xmlEncoded | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/AltText |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CompanionClickThrough |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CompanionClickTracking |  | - | 3.0 | 4.0 | 4.1 | 
|  | id | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | event | 2.0 | 3.0 | 4.0 | 4.1 | 
|  |  |  |  |  |  | 
|  |  |  |  |  |  | 
|  |  |  |  |  |  | 
|  |  |  |  |  |  | 
| Elements | Attributes | Version Support |  |  |  | 
| VAST/Ad/Wrapper |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | followAdditionalWrappers | - | - | 4.0 | 4.1 | 
|  | allowMultipleAds | - | - | 4.0 | 4.1 | 
|  | fallbackOnNoAd | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Impression |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/VASTAdTagURI |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/AdSystem |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | version | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Pricing |  | - | - | 4.0 | 4.1 | 
|  | model | - | - | 4.0 | 4.1 | 
|  | currency | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Error |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/ViewableImpression |  | - | - | 4.0 | 4.1 | 
|  | id | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Viewable |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NotViewable |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ViewUndetermined |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/AdVerifications |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Verification |  | - | - | 4.0 | 4.1 | 
|  | vendor | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ViewableImpression |  | - | - | 4.0 | - | 
|  | id | - | - | 4.0 | - | 
| &nbsp;&nbsp;&nbsp;/Extensions |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Extension |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;/Creatives |  | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Creative |  | 2.0 | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
|  | sequence |  | 3.0 | 4.0 | 4.1 | 
|  | adId | 2.0 | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Linear |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  |  | 3.0 | 4.0 | 4.1 | 
|  | event |  | 3.0 | 4.0 | 4.1 | 
|  | offset |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/VideoClicks |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ClickTracking |  |  | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CustomClick |  |  | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Icons |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Icon |  | - | 3.0 | 4.0 | 4.1 | 
|  | program | - | 3.0 | 4.0 | 4.1 | 
|  | width | - | 3.0 | 4.0 | 4.1 | 
|  | height | - | 3.0 | 4.0 | 4.1 | 
|  | xPosition | - | 3.0 | 4.0 | 4.1 | 
|  | yPosition | - | 3.0 | 4.0 | 4.1 | 
|  | duration | - | 3.0 | 4.0 | 4.1 | 
|  | offset | - | 3.0 | 4.0 | 4.1 | 
|  | apiFramework | - | 3.0 | 4.0 | 4.1 | 
|  | pxratio | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/StaticResource |  | - | 3.0 | 4.0 | 4.1 | 
|  | creativeType | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IFrameResource |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/HTMLResource |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconClicks |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconClickThrough |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconClickTracking |  | - | 3.0 | 4.0 | 4.1 | 
|  | id | - | - | - | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IconViewTracking |  | - | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/InteractiveCreativeFile |  | - | - | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinearAds |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinear |  |  | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | - | - | 
|  | width |  | 3.0 | - | - | 
|  | height |  | 3.0 | - | - | 
|  | expandedWidth |  | 3.0 | - | - | 
|  | expandedHeight |  | 3.0 | - | - | 
|  | scalable |  | 3.0 | - | - | 
|  | maintainAspectRatio |  | 3.0 | - | - | 
|  | minSuggestedDuration |  | 3.0 | - | - | 
|  | apiFramework |  | 3.0 | - | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinearClickThrough |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/NonLinearClickTracking |  |  | 3.0 | 4.0 | 4.1 | 
|  | id | - | - | - | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  |  | 3.0 | 4.0 | 4.1 | 
|  | event |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CompanionAds |  |  | 3.0 | 4.0 | 4.1 | 
|  | required |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Companion |  |  | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
|  | width |  | 3.0 | 4.0 | 4.1 | 
|  | height |  | 3.0 | 4.0 | 4.1 | 
|  | assetWidth |  | 3.0 | 4.0 | 4.1 | 
|  | assetHeight |  | 3.0 | 4.0 | 4.1 | 
|  | expandedWidth |  | 3.0 | 4.0 | 4.1 | 
|  | expandedHeight |  | 3.0 | 4.0 | 4.1 | 
|  | apiFramework |  | 3.0 | 4.0 | 4.1 | 
|  | adSlotID |  | 3.0 | 4.0 | 4.1 | 
|  | pxratio |  | - | 4.0 | 4.1 | 
|  | logoTile | - | - | - | - | 
|  | logoTitle | - | - | - | - | 
|  | logoArtist | - | - | - | - | 
|  | logoURL | - | - | - | - | 
|  | renderingMode | - | - | - | - | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/StaticResource |  |  | 3.0 | 4.0 | 4.1 | 
|  | creativeType |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/IFrameResource |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/HTMLResource |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/AdParameters |  |  | 3.0 | 4.0 | 4.1 | 
|  | xmlEncoded |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/AltText |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CompanionClickThrough |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CompanionClickTracking |  |  | 3.0 | 4.0 | 4.1 | 
|  | id |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/TrackingEvents |  |  | 3.0 | 4.0 | 4.1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/Tracking |  |  | 3.0 | 4.0 | 4.1 | 
|  | event |  | 3.0 | 4.0 | 4.1 | 
