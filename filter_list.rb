def filter_list(l)
  l.select { |i| i.is_a?(Integer) }
end

puts filter_list([1, 'dois', 3, 'quatro', 5, 'seis'])
