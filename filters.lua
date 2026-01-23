function Image (el)
  return {}
end

function RawBlock(el)
  return {}
end

function RawInline(el)
  return {}
end

function Span (el)
  if #el.content == 0 then
    return {}
  end
end

function Div (el)
  if #el.content == 0 then
    return {}
  end

  return el.content
end

function remove_attrs(el)
  if el.attr then
    el.attr = {}
  end
  return el
end

function Code(el)
  return remove_attrs(el)
end

function CodeBlock(el)
  return remove_attrs(el)
end
