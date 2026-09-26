class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.tag = tag
        # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.value = value
        # A list of HTMLNode objects representing the children of this node
        self.children = children
        # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented!")

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )

