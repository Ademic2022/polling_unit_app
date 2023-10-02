$(document).ready(function() {
    // Click event for the "Select All" button
    $('#select_all').click(function() {
        // Check all checkboxes
        $('.lga-checkbox').prop('checked', true);
    });

    $('#select-lgas-button').click(function() {
        var selectedLGAs = [];
        $('.lga-checkbox:checked').each(function() {
            var lgaId = $(this).data('id');
            selectedLGAs.push(lgaId);
            // console.log(selectedLGAs);
        });

        // Send selectedLGAs to the backend using AJAX
        $.ajax({
            type: 'POST',
            url: '/summed_results',
            data: JSON.stringify({ 'selected_lgas': selectedLGAs }),
            contentType: 'application/json',
            success: function(response) {
                // Handle the response from the server
                displayResults(response.summed_results);
                
            },
            error: function(error) {
                console.error(error);
            }
        });
    });

    function displayResults(summedResults) {
        var tableBody = $('#results-table tbody');
        tableBody.empty(); // Clear any previous results

        for (var party in summedResults) {
            if (summedResults.hasOwnProperty(party)) {
                var score = summedResults[party];
                var row = '<tr><td>' + party + '</td><td>' + score + '</td></tr>';
                tableBody.append(row);
            }
        }
    }
});
