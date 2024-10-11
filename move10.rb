def move_ten(str)
  str.each_char.map do |char|
    char_unicode = char.ord
    char_unicode += 10
    if char_unicode > 122
      restante = char_unicode - 122
      new_code = (restante + 97) - 1
    else
      new_code = char_unicode
    end
    new_code.chr(Encoding::UTF_8)
  end.join
end

puts move_ten('testecase')
