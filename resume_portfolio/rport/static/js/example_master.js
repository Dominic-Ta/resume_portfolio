$(document).ready(function() {
    $('#netflix_data').DataTable({
        responsive: true,
        searchPanes: {
            columns: [2,4,5,6],
            dtOpts: {
                select: {
                    style: 'multi'
                }
            }
        },
        dom: 'Plfrtip'
    });
});