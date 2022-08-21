adaptive card

[TOC]



# Proposal

## Architecture

As a simple GUI framework, adaptive card can replace some of traditional MFC GUIs

In the whole system, the adaptive card is in the GUI layer, which is the same layer as MFC



layers:

- GUI Appl layer
- GUI framework layer
- ITF/APT layer



![Architecture](http://www.plantuml.com/plantuml/png/bP7DQiCm48JlUeebzz0tA34kAO8634rEfOUjlJOY-X6hTKefVVSQ5ug4CKckkpFIDxEx9CWoEgiYjcSS23RF9mrLZ1OiVX5lu5i1l3qPz269QHCq77fZ2Lv9nFW1ffKDm_kieejf2IeHPlCn2kNB5qBse7qVycbbXmOPJlf_-ADAbfxHqMVWSm5qsDT__WwZc0j1ZToLPdtSFrJDiR1fdo8SGZTQckrrS2xuVBBCC256v4AptWPFcfHfiu35EpEgkg5Ns6uV5p5lzTs1ce6k_xmkMusvBBGqJeUyBhfw5ALsvBlHsLy0)

## Adaptive card module

Adaptive card does not provide C library (??). We need implement the C binding based on its provided libraries, either

- JavaScript Lib
- .NET lib
- UWP lib (Is it feasible?)

Pros and Cons of different libraries

- Javascript Lib
  - Pros: Cross platform. More popular. Easier to learn
  - Cons: Performance may be a problem when there are lots of GUI elements
- .NET lib
  - Pros: The Cons of javascript lib
  - Cons: The Pros of javascript lib

### API design

We need implement C/C++ binding for the library

We can implement the full set of APIs, or just selectively implement some of them. 

Below is the full set of API

- AdaptiveCard API
  - Refder https://docs.microsoft.com/en-us/adaptive-cards/sdk/authoring-cards/net


```cpp
class AdaptiveCard
{
    public:
// Description: To construct an AdaptiveCard from JSON String
// Parameters
// 		JSONString: the JSON String that describing the card
// Returns:
// 		NA
// throws:
//		std::exception      
    explicit AdaptiveCard(JSONString) ;
// Description: To add an element to the AdaptiveCard
// Parameters
// 		Element: the element to be added
// Returns:
// 		NA
// throws:
//		std::exception    
    void Add(Element);
    
// Description: To add an element to the AdaptiveCard
// Parameters
// 		Element: the element to be added
// Returns:
// 		JSONString: the JSON string of the adaptive card
// throws:
//		std::exception      
    JSONString ToJson();
};

// Element API
// ...
```

- Template API
  - Refer https://docs.microsoft.com/en-us/adaptive-cards/templating/sdk for the major concepts

```cpp
class AdaptiveCardTemplate
{
    public:
// Description: To construct a template
// Parameters
// 		JSONString: the JSON string that describing the template
// Returns:
// 		NA
// throws:
//		std::exception
    explicit AdaptiveCardTemplate(JSONString);
    
// Description: To expand a template
// Parameters
// 		JSONString: the JSON string that describing the payload
// Returns:
// 		JSONString: the JSON string that describing the adaptive card
// throws:
//		std::exception    
    JSONString expand(JSONString);
}
```

- Render API

  - Refer https://docs.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/javascript/render-a-card

```cpp
// Description: To show a adaptive card dialog. It is a blocking dialog
// Parameters
// 		HWND: the parent window
// 		onExecuteAction: the adaptive card's event handlers. onExecuteAction is invoked
// 			whenever an action is clicked in the card
// 		JSONString: the JSON string that describing the card
// Returns:
// 		NA
// throws:
//		std::exception
void ShowAdaptiveCardModelDialog(HWND, onExecuteAction, AdaptiveCard);
// Description: To show a adaptive card dialog. It is a modelless dialog
void ShowAdaptiveCardModellessDialog(HWND, onExecuteAction, AdaptiveCard);
```

### C binding

Different library's C binding technology is different

- Javascript library: 
  - Use [WebView2](https://docs.microsoft.com/en-us/microsoft-edge/webview2/) to host web view in native app
  - a [guide line](https://docs.microsoft.com/en-us/microsoft-edge/webview2/get-started/win32) from MS

- .NET
  - refer https://stackoverflow.com/questions/4428267/calling-c-sharp-from-c


## algparUI dialog

Layers of algparUI dialog:

- AlgparUI dialog: the GUI part

- AlgparUI algpar module: the non GUI part

  

AlgparUI dialog Main Flow

- It reads config using `AlgparUI algpar module` to AlgParUIConfig type
- It converts/serialize AlgParUIConfig type to adaptive card required JSON format string
- It implements display  using`Adaptive Card` module
- It gets the user input from `Adaptive Card` module, then convert the data to CFG format, then save to file



Q: Why not impl all code in UI layer

Because inspection module depending on AlgparUI functions, So there must be some code in ITF layer



Q: Why not impl all code in ITF layer

Because it is not feasible to implement GUI in ITF layer. In order to support porting to different GUIs, ITF layer must not depend on the implementation of GUI



Q: Why not use JSON in all layers?

Because we still use algpar module in ITF layer. It is CFG format

To satisfy adaptive card requirement, we can 

- either convert our data type to JSON format
- or create AdaptiveCard object directly

