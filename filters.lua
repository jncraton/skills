function Image (el)
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
end
